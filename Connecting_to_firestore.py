import firebase_admin
from firebase_admin import (credentials, firestore)
from datetime import datetime
import pytz

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