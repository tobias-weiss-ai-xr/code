# pip install adafruit-blinka to get board library
import time
import json
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

max_val = None
min_val = None

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
channels = [AnalogIn(ads, ADS.P0), AnalogIn(ads, ADS.P1)]

print("------{:>5}\t{:>5}".format("raw", "v"))
while True:
    for i, chan in enumerate(channels):
        print(f"{i}: {chan.value}, {chan.voltage}")
        time.sleep(0.5)
