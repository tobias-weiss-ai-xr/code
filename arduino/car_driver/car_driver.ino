//declaring the pins for the IN pins on the L298N
const int rightForwardPin = 5;
const int rightBackwardPin = 7;
const int leftBackwardPin = 9;
const int leftForwardPin = 11;

int runTime = 5000;

void setup() {
  //Stating that the pins are OUTPUT
  pinMode(rightForwardPin, OUTPUT);
  pinMode(rightBackwardPin, OUTPUT);
  pinMode(leftForwardPin, OUTPUT);
  pinMode(leftBackwardPin, OUTPUT);
}

//Looping to test the wheels of the car
void loop() {

  forward();
 
  stopCar();
 
  backward();
 
  stopCar();
 
  left();
 
  stopCar();
 
  right();
 
  stopCar();
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

//Setting the wheels to go right by setting the rightBackwardPin and leftForwardPin to HIGH
void right(){
  digitalWrite(rightForwardPin, LOW);
  digitalWrite(rightBackwardPin, HIGH);
  digitalWrite(leftForwardPin, HIGH);
  digitalWrite(leftBackwardPin, LOW);
  delay(runTime);
}

//Setting the wheels to go left by setting the rightForwardPin and leftBackwardPin to HIGH
void left(){
  digitalWrite(rightForwardPin, HIGH);
  digitalWrite(rightBackwardPin, LOW);
  digitalWrite(leftForwardPin, LOW);
  digitalWrite(leftBackwardPin, HIGH);
  delay(runTime);
}

//Setting the wheels to go stop by setting all the pins to LOW
void stopCar(){
  digitalWrite(rightForwardPin, LOW);
  digitalWrite(rightBackwardPin, LOW);
  digitalWrite(leftForwardPin, LOW);
  digitalWrite(leftBackwardPin, LOW);
  delay(1000);
}
