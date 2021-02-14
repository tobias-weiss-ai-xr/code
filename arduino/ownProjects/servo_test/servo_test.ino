/*
example 2.1 – digital thermometer
Created 14/04/2010 —  By John Boxall — http://tronixstuff.wordpress.com —  CC by-sa v3.0
Uses an Analog Devices TMP36 temperature sensor to measure temperature and output values to the serial connection
Pin 1 of TMP36 to Arduino 5V power socket
Pin 2 of TMP36 to Arduino analog 0 socket
Pin 3 of TMP36 to Arduino GND socket
*/
void setup()
{
Serial.begin(9600);   // activate the serial output connection
}
float voltage = 0; // setup some variables
float sensor = 0;
float celsius = 0;
float fahrenheit = 0;

void loop()
{
sensor = analogRead(A0);
voltage = (((5000/1024)*sensor)-500);
celsius = (voltage-500)/10;
Serial.println("voltage:");
Serial.println(voltage);
Serial.println("celsius:");
Serial.println(celsius, 5);
delay(1000);
//voltage = (sensor*5000)/1024;
//voltage = voltage-500;
//celsius = voltage/10;
//fahrenheit = ((celsius * 1.8)+32);
//Serial.print("Temperature: ");
//Serial.print(celsius,2);
//Serial.println(" degrees C");
//Serial.print("Temperature: ");
//Serial.print(fahrenheit,2);
//Serial.println(" degrees F");
//Serial.println("_ _ _ _ _ _ _ _ _ _ _ _ _ _  ");
//delay (1000);
}
