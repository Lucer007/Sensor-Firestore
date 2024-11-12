import firebase_admin
from firebase_admin import (credentials, firestore)

# Making a function to be able to export
def Connect_to_firestore():
    # Initialize Firestore with your service account key
    cred = credentials.Certificate(r"C:\Users\lc201\Documents\Python Project\Sensor-Firestore\save-a-slot-firebase-adminsdk-xeee6-864bff52bb.json")
    firebase_admin.initialize_app(cred)

    # Now you can interact with your Firestore database
    db = firestore.client()

