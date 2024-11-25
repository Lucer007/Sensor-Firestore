import serial
import time

def control_arduino_led_red(port='COM4', baud_rate=9600, on_time=5, off_time=1):
    # Set up the serial connection to the Arduino (change COM port to match your system)
    # On Windows, it could be something like 'COM3', on Linux, it could be '/dev/ttyACM0' or '/dev/ttyUSB0'
    arduino = serial.Serial('COM4', 9600, timeout=1)

    # Wait for the serial connection to initialize
    time.sleep(2)

    # Send a command to turn the LED on (sending '1')
    arduino.write(b'A')

def control_arduino_led_green(port='COM4', baud_rate=9600, on_time=5, off_time=1):
    # Set up the serial connection to the Arduino (change COM port to match your system)
    # On Windows, it could be something like 'COM3', on Linux, it could be '/dev/ttyACM0' or '/dev/ttyUSB0'
    arduino = serial.Serial('COM4', 9600, timeout=1)

    # Wait for the serial connection to initialize
    time.sleep(2)

    # Send a command to turn the LED on (sending '1')
    arduino.write(b'B')

def control_arduino_led_red2(port='COM4', baud_rate=9600, on_time=5, off_time=1):
    # Set up the serial connection to the Arduino (change COM port to match your system)
    # On Windows, it could be something like 'COM3', on Linux, it could be '/dev/ttyACM0' or '/dev/ttyUSB0'
    arduino = serial.Serial('COM4', 9600, timeout=1)

    # Wait for the serial connection to initialize
    time.sleep(2)

    # Send a command to turn the LED on (sending '1')
    arduino.write(b'D')

def control_arduino_led_green2(port='COM4', baud_rate=9600, on_time=5, off_time=1):
    # Set up the serial connection to the Arduino (change COM port to match your system)
    # On Windows, it could be something like 'COM3', on Linux, it could be '/dev/ttyACM0' or '/dev/ttyUSB0'
    arduino = serial.Serial('COM4', 9600, timeout=1)

    # Wait for the serial connection to initialize
    time.sleep(2)

    # Send a command to turn the LED on (sending '1')
    arduino.write(b'E')