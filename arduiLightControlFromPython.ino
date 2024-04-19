const int RED_PIN = 2;
const int GREEN_PIN = 4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    String msg = Serial.readString();

    if(msg == "ON"){
      digitalWrite(GREEN_PIN, HIGH);
      digitalWrite(RED_PIN, LOW);
    }else if(msg == "OFF"){
      digitalWrite(GREEN_PIN, LOW);
      digitalWrite(RED_PIN, HIGH);
    }else{
      for(int i = 0; i < 5; ++i){
        digitalWrite(RED_PIN, HIGH);
        delay(100);
        digitalWrite(RED_PIN, LOW);
        delay(100);
      }
    }

  }
}
