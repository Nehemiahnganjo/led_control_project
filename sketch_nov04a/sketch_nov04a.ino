const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read the incoming command
    if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Turn LED on
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);   // Turn LED off
    }
  }
}
