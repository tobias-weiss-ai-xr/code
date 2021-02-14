// Projekt1: LED-Laola

//Config
int led1=2;
int led2=3;
int led3=4;
int led4=5;
int led5=6;

int d=250; //Delay

void setup() {
  // init Ports:
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led1, HIGH);
  delay(d);
  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  delay(d);
  digitalWrite(led2, LOW);
  digitalWrite(led3, HIGH);
  delay(d);
  digitalWrite(led3, LOW);
  digitalWrite(led4, HIGH);
  delay(d);
  digitalWrite(led4, LOW);
  digitalWrite(led5, HIGH);
  delay(d);
  digitalWrite(led5, LOW);
}
