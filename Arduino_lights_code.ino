const int ledPin12 = 12; // red
const int ledPin13 = 13; // green

void setup() {
  pinMode(ledPin12, OUTPUT);
  pinMode(ledPin13, OUTPUT);
  digitalWrite(ledPin12, LOW);
  digitalWrite(ledPin13, LOW);

  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the incoming command

    if (command == 'A') {// command a slot is available
      // Turn ON LED on pin 12, OFF on pin 13
      digitalWrite(ledPin12, HIGH);
      digitalWrite(ledPin13, LOW);
    } else if (command == 'B') { //command b slot is unavailable
      // Turn OFF LED on pin 12, ON on pin 13
      digitalWrite(ledPin12, LOW);
      digitalWrite(ledPin13, HIGH);
    } else if (command == 'C') {
      // Turn OFF both LEDs
      digitalWrite(ledPin12, LOW);
      digitalWrite(ledPin13, LOW);
    }
  }
}


