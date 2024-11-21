import serial
import firebase_admin
from firebase_admin import credentials, firestore, db
from datetime import datetime
from Connecting_to_firestore import connect_to_firestore

connect_to_firestore = connect_to_firestore()

# Initialize Serial Connection to Arduino
arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Replace with your port

while True:
    if arduino.in_waiting > 0:
        sensor_value = arduino.readline().decode('utf-8').strip()
        if sensor_value.isdigit():
            # Add data to Firestore
            doc_ref = db.collection("beam_status").document()
            doc_ref.set({
                "sensor_value": int(sensor_value),
                "timestamp": datetime.now()
            })
            print(f"Uploaded {sensor_value} to Firestore")
