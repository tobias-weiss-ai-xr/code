//declaring the pins for the IN pins on the L298N
const int rightForwardPin = 11;
const int rightBackwardPin = 9;
const int leftForwardPin = 7;
const int leftBackwardPin = 5;


int runTime=500;

void setup() {
  //Stating that the pins are OUTPUT
  pinMode(rightForwardPin, OUTPUT);
  pinMode(rightBackwardPin, OUTPUT);
  pinMode(leftForwardPin, OUTPUT);
  pinMode(leftBackwardPin, OUTPUT);
}

void loop(){
  forward();
  backward();
}

//Setting the wheels to go forward by setting the forward pins to HIGH
void forward(){
  digitalWrite(rightForwardPin, HIGH);
  digitalWrite(rightBackwardPin, LOW);
  digitalWrite(leftForwardPin, HIGH);
  digitalWrite(leftBackwardPin, LOW);
  delay(runTime);
}

//Setting the wheels to go backward by setting the backward pins to HIGH
void backward(){
  digitalWrite(rightForwardPin, LOW);
  digitalWrite(rightBackwardPin, HIGH);
  digitalWrite(leftForwardPin, LOW);
  digitalWrite(leftBackwardPin, HIGH);
  delay(runTime);
}
