import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import pytz
import time
from Sensor_led import control_arduino_led_red, control_arduino_led_green, control_arduino_led_red2, control_arduino_led_green2

def firstconnect_to_firestore():
    # Initialize Firestore with your service account key
    cred = credentials.Certificate(
        r"C:\Users\lc201\Documents\Python Project\Sensor-Firestore\save-a-slot-firebase-adminsdk-xeee6-a6a543c43c.json")
    firebase_admin.initialize_app(cred)

    # Now you can interact with your Firestore database
    db = firestore.client()
    return db

def connect_to_firestore():
    # need to call the database again without initializing it once more
    db = firestore.client()
    return db

def get_slot_reservations(slot_id):
    db = connect_to_firestore()
    # Reference to the Reservations collection
    reservations_ref = db.collection('Reservations')

    try:
        # Query for all reservations with the specified slot_id
        # Note: Changed slot_id to match Firestore format (Slot1 instead of slot1)
        formatted_slot_id = f"Slot{slot_id[-1]}"
        query = reservations_ref.where('slotID', '==', formatted_slot_id).order_by('reservationStartTime').get()

        reservation_list = []
        for doc in query:
            data = doc.to_dict()
            if 'reservationStartTime' in data and 'reservationEndTime' in data:
                # Convert string times to datetime objects
                data['reservationStartTime'] = datetime.strptime(
                    data['reservationStartTime'],
                    '%Y-%m-%dT%H:%M'
                ).replace(tzinfo=pytz.UTC)

                data['reservationEndTime'] = datetime.strptime(
                    data['reservationEndTime'],
                    '%Y-%m-%dT%H:%M'
                ).replace(tzinfo=pytz.UTC)

                reservation_list.append(data)

        return reservation_list
    except Exception as e:
        print(f"Error retrieving reservations: {e}")
        return []


def check_current_reservation_status(slotID):
    # Get current time in UTC
    current_time = datetime.now(pytz.UTC)
    print(f"Checking slot {slotID} at {current_time}")

    try:
        # Query the collection for reservations matching the slotID
        db = connect_to_firestore()
        reservations = (
            db.collection('reservations')  # Replace with your actual collection name
            .where('slotID', '==', slotID)
            .get()
        )

        if not reservations:
            print(f"No reservations found for slot {slotID}")
            return False

        # Check each reservation for the slot
        for reservation in reservations:
            reservation_data = reservation.to_dict()

            # Parse the timestamp strings to datetime objects
            start_time = datetime.strptime(
                reservation_data['reservationStartTime'],
                "%Y-%m-%dT%H:%M"
            ).replace(tzinfo=pytz.UTC)

            end_time = datetime.strptime(
                reservation_data['reservationEndTime'],
                "%Y-%m-%dT%H:%M"
            ).replace(tzinfo=pytz.UTC)

            print(f"Comparing: Start: {start_time}, Current: {current_time}, End: {end_time}")

            # Check if there's an active reservation
            if start_time <= current_time <= end_time:
                print(f"Found active reservation for slot {slotID}")
                return True

        print(f"No active reservations for slot {slotID}")
        return False

    except Exception as e:
        print(f"Error checking reservation status: {e}")
        return False

def monitor_parking_slots():
    # Initialize Firebase connection
    db = firstconnect_to_firestore()

    print("Starting parking slot monitoring system (Eastern Time)")
    print("Press Ctrl+C to stop the program")

    slots = ["slot1", "slot2"]
    last_status = {slot: None for slot in slots}

    try:
        while True:
            current_time = get_current_eastern_time()
            print(f"\nChecking slots at {current_time.strftime('%Y-%m-%d %H:%M:%S')} ET")

            # Get all reservations once per cycle
            all_reservations = get_all_reservations()

            for slot in slots:
                try:
                    slot_status = check_slot_status(slot, current_time, all_reservations)

                    # Only update and print if status has changed
                    if slot_status != last_status[slot]:
                        if not slot_status:
                            print(f"Parking {slot} is now AVAILABLE")
                            if slot == "slot1":
                                control_arduino_led_green()
                                print()
                            else:
                                control_arduino_led_green2()
                                print()
                        else:
                            print(f"Parking {slot} is now OCCUPIED")
                            if slot == "slot1":
                                control_arduino_led_red()
                                print()
                            else:
                                control_arduino_led_red2()
                                print()

                        last_status[slot] = slot_status

                except Exception as e:
                    print(f"Error checking {slot}: {e}")
                    continue

            time.sleep(1)  # Check every 5 seconds

    except KeyboardInterrupt:
        print("\nGracefully shutting down parking monitor...")
    except Exception as e:
        print(f"Critical error in monitoring system: {e}")
        raise
    finally:
        print("Monitoring system stopped")

def check_slot_status(slot_id, current_time, reservations):
    # Filter reservations for the specific slot
    slot_reservations = [r for r in reservations if r['slotID'] == f"Slot{slot_id[-1]}"]

    for reservation in slot_reservations:
        if reservation['reservationStartTime'] <= current_time <= reservation['reservationEndTime']:
            return True  # Slot is occupied
    return False  # Slot is available

def get_all_reservations():
    db = firestore.client()
    reservations_ref = db.collection('Reservations')
    eastern = pytz.timezone('America/New_York')

    try:
        # Get all reservations and sort them by startTime
        query = reservations_ref.order_by('reservationStartTime').get()

        reservations = []
        for doc in query:
            data = doc.to_dict()
            if 'reservationStartTime' in data and 'reservationEndTime' in data:
                # Convert string times to Eastern Time datetime objects
                start_time = datetime.strptime(
                    data['reservationStartTime'],
                    '%Y-%m-%dT%H:%M'
                )
                end_time = datetime.strptime(
                    data['reservationEndTime'],
                    '%Y-%m-%dT%H:%M'
                )

                # Localize the naive datetime to Eastern Time
                start_time = eastern.localize(start_time)
                end_time = eastern.localize(end_time)

                data['reservationStartTime'] = start_time
                data['reservationEndTime'] = end_time
                reservations.append(data)

        return reservations
    except Exception as e:
        print(f"Error retrieving reservations: {e}")
        return []

def get_current_eastern_time():
    # Get current UTC time
    utc_now = datetime.now(pytz.UTC)
    # Convert to Eastern Time
    eastern = pytz.timezone('America/New_York')
    return utc_now.astimezone(eastern)