// Projekt1: LED-Laola

int d=250; //Delay

void setup() {
  // init Ports:
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i=2;i<7;i++)
  {
    digitalWrite(i, HIGH);
    delay(d);
    digitalWrite(i, LOW);
    delay(d);
  }
}
