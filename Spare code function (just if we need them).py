def add_parking_slot_data(slot_id, availability, location):
    db = connect_to_firestore()
    # Reference to the parking slots collection
    doc_ref = db.collection(u'ParkingSlots').document(slot_id)

    # Data to send to Firestore
    data = {
        u'availability': availability,
        u'location': location,
        u'timestamp': firestore.SERVER_TIMESTAMP  # adds the server timestamp
    }

    # Add data to Firestore
    doc_ref.set(data)
    print(f"Data added to document with ID: {slot_id}")

def get_parking_slot_data(slot_id):
    db = connect_to_firestore()
    slot_id = "slot22"
    # Reference to the specific document in the ParkingSlots collection
    doc_ref = db.collection(u'ParkingSlots').document(slot_id)

    try:
        # Retrieve the document data
        doc = doc_ref.get()
        if doc.exists:
            # Print the document data
            data = doc.to_dict()
            print(f"Data for slot {slot_id}:")
            print(f"Availability: {data.get('availability')}")
            print(f"Location: {data.get('location')}")
            print(f"Timestamp: {data.get('timestamp')}")
        else:
            print(f"No document found with ID: {slot_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

firstconnect_to_firestore()
slot1 = get_parking_slot_data(slot_id="slot22")
slot2 = get_parking_slot_data(slot_id="slot23")
starting = input("Starting the script to check the slot availability\n Please Enter true to start :")
while starting == "true":
    if slot1['availability'] :
        control_arduino_led_green()
        print("Parking slot available")
        slot1 = checking_availability(slot_id="slot22")
    else:
        control_arduino_led_red()
        print("Parking slot not available")
        slot1 = checking_availability(slot_id="slot22")

    if slot2['availability']:
        control_arduino_led_green2()
        print("Parking slot2 available")
        slot2 = checking_availability(slot_id="slot23")
    else:
        control_arduino_led_red2()
        print("Parking slot2 not available")
        slot2 = checking_availability(slot_id="slot23")