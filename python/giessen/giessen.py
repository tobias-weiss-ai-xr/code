#/usr/bin/env python3
import RPi.GPIO as GPIO 
from time import sleep 

pin = 4

GPIO.setmode(GPIO.BCM) 
 
try:
    GPIO.setup(pin, GPIO.OUT) 
    sleep(3) 
    GPIO.setup(pin, GPIO.IN) 
#    sleep(15) 
#    GPIO.setup(pin, GPIO.OUT) 
#    sleep(3) 
#    GPIO.setup(pin, GPIO.IN) 
except:
    GPIO.setup(pin, GPIO.IN) 
    GPIO.cleanup()
