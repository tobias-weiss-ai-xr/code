int a1_rot = 2;
int a1_gelb = 3;
int a1_gruen = 4;
int a1_taster = 8;
int a1_stat = 0;

int a2_rot = 5;
int a2_gelb = 6;
int a2_gruen = 7;
int a2_taster = 9;
int a2_stat = 0;

int act_stat = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(a1_rot, OUTPUT);
  pinMode(a1_gelb, OUTPUT);
  pinMode(a1_gruen, OUTPUT);
  pinMode(a1_taster, INPUT);
  pinMode(a2_rot, OUTPUT);
  pinMode(a2_gelb, OUTPUT);
  pinMode(a2_gruen, OUTPUT);
  pinMode(a2_taster, INPUT);

  digitalWrite(a1_rot, HIGH);
  digitalWrite(a2_gruen, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  a1_stat = digitalRead(a1_taster);
  a2_stat = digitalRead(a2_taster);
  Serial.print("a1_stat:");
  Serial.println(a1_stat); 
  Serial.print("a2_stat:");
  Serial.println(a2_stat); 
  delay(1000);
  if(a1_stat == HIGH && act_stat != 1){
    digitalWrite(a2_gruen, LOW);
    digitalWrite(a2_gelb, HIGH);
    delay(2000);
    digitalWrite(a2_gelb, LOW);
    digitalWrite(a2_rot, HIGH);
    delay(4000);
    digitalWrite(a1_rot, LOW);
    digitalWrite(a1_gelb, HIGH);
    delay(2000);
    digitalWrite(a1_gelb, LOW);
    digitalWrite(a1_gruen, HIGH);
    act_stat = 1;
  } else if (a2_stat == HIGH && act_stat != 2) {
    digitalWrite(a1_gruen, LOW);
    digitalWrite(a1_gelb, HIGH);
    delay(2000);
    digitalWrite(a1_gelb, LOW);
    digitalWrite(a1_rot, HIGH);
    delay(4000);
    digitalWrite(a2_rot, LOW);
    digitalWrite(a2_gelb, HIGH);
    delay(2000);
    digitalWrite(a2_gelb, LOW);
    digitalWrite(a2_gruen, HIGH);
    act_stat = 2;
  }
}
