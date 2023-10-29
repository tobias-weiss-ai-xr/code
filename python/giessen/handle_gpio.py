import RPi.GPIO as GPIO
import time
from time import sleep
import sys

def handle_gpio(pin, duration):
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    sleep(duration)
    GPIO.output(pin, 0)

if __name__ == "__main__":
    #TODO: switch to argparse
    print(sys.argv)
    handle_gpio(pin=int(sys.argv[1]), duration=int(sys.argv[2]))
    GPIO.cleanup()
