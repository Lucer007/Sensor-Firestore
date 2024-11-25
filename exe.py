from Connecting_to_firestore import get_parking_slot_data, checking_availability, firstconnect_to_firestore
from Sensor_led import control_arduino_led_red, control_arduino_led_green, control_arduino_led_red2, control_arduino_led_green2

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