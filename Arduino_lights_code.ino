const int ledPin10 = 10; // red
const int ledPin11 = 11; // green
const int ledPin12 = 12; // red
const int ledPin13 = 13; // green


void setup() {
  pinMode(ledPin10, OUTPUT);
  pinMode(ledPin11, OUTPUT);
  pinMode(ledPin12, OUTPUT);
  pinMode(ledPin13, OUTPUT);
  digitalWrite(ledPin10, LOW);
  digitalWrite(ledPin11, LOW);
  digitalWrite(ledPin12, LOW);
  digitalWrite(ledPin13, LOW);

  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the incoming command

    if (command == 'A') {// command a slot1 is available
      // Turn ON LED on pin 12, OFF on pin 13
      digitalWrite(ledPin12, HIGH);
      digitalWrite(ledPin13, LOW);
    } else if (command == 'B') { //command b slot1 is unavailable
      // Turn OFF LED on pin 12, ON on pin 13
      digitalWrite(ledPin12, LOW);
      digitalWrite(ledPin13, HIGH);
    } else if (command == 'C') {
      // Turn OFF both LEDs
      digitalWrite(ledPin12, LOW);
      digitalWrite(ledPin13, LOW);
    } else if (command == 'D') { //command d slot2 is available
      // Turn ON LED on pin 10, OFF on pin 11
      digitalWrite(ledPin10, HIGH);
      digitalWrite(ledPin11, LOW);
    } else if (command == 'E') { //command e slot2 is unavailable
      // Turn OFF LED on pin 10, ON on pin 11
      digitalWrite(ledPin10, LOW);
      digitalWrite(ledPin11, HIGH);
    }
    }
  }


