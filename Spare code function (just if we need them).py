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
