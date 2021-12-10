const int  LED_PIN = 10;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

byte inputData;
void loop() {
  if (Serial.available() > 0) {
    inputData = Serial.read();
    switch (inputData) {
      case '0':
        digitalWrite(LED_PIN, LOW);
        Serial.println("turn off");
        break;
      case '1':
        digitalWrite(LED_PIN, HIGH);
        Serial.println("turn on");
        break;
      default:
        break;
    }
  }
}
