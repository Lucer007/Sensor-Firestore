import firebase_admin
from firebase_admin import (credentials, firestore)

# Making a function to be able to export
def connect_to_firestore():
    # Initialize Firestore with your service account key
    cred = credentials.Certificate(r"C:\Users\lc201\Documents\Python Project\Sensor-Firestore\save-a-slot-firebase-adminsdk-xeee6-864bff52bb.json")
    firebase_admin.initialize_app(cred)

    # Now you can interact with your Firestore database
    db = firestore.client()
    return db


def add_parking_slot_data(slot_id, availability, location):
    db = connect_to_firestore()
    # Reference to the parkingslots collection
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


# Example usage:
add_parking_slot_data("slot22", "available", "Zone A")


