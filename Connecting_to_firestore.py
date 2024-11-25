import firebase_admin
from firebase_admin import (credentials, firestore)

def firstconnect_to_firestore():
    # Initialize Firestore with your service account key
    cred = credentials.Certificate(
        r"C:\Users\lc201\Documents\Python Project\Sensor-Firestore\save-a-slot-firebase-adminsdk-xeee6-864bff52bb.json")
    firebase_admin.initialize_app(cred)

    # Now you can interact with your Firestore database
    db = firestore.client()
    return db

def connect_to_firestore():
    # need to call the database again without initializing it once more
    db = firestore.client()
    return db

def get_parking_slot_data(slot_id):
    db = connect_to_firestore()
    # Reference to the specific document in the ParkingSlots collection
    doc_ref = db.collection(u'ParkingSlots').document(slot_id)

    try:
        # Retrieve the document data
        doc = doc_ref.get()
        if doc.exists:
            data = doc.to_dict()
            return data
        else:
            print(f"No document found with ID: {slot_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

def checking_availability(slot_id):
    db = connect_to_firestore()
    # Reference to the specific document in the ParkingSlots collection
    doc_ref = db.collection(u'ParkingSlots').document(slot_id)

    try:
        # Retrieve the document data
        doc = doc_ref.get()
        if doc.exists:
            # Print the document data
            doc.to_dict()
            return doc.to_dict()
        else:
            print(f"No document found with ID: {slot_id}")
    except Exception as e:
        print(f"An error occurred: {e}")



