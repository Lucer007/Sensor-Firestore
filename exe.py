from Connecting_to_firestore import get_parking_slot_data, checking_availability
from Sensor_led import control_arduino_led_red, control_arduino_led_green


slot1 = get_parking_slot_data(slot_id="slot22")
starting = input("Starting the script to check the slot availability\n PLease Enter True to start :")
while starting == "true":
    if slot1['availability'] == "available":
        control_arduino_led_green()
        print("Parking slot available")
        Park = checking_availability(slot_id="slot22")
    else:
        control_arduino_led_red()
        print("Parking slot not available")
        slot1 = checking_availability(slot_id="slot22")
