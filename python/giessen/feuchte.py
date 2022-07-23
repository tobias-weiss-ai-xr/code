# Simple demo of continuous ADC conversion mode for channel 0 of the ADS1x15 ADC.
# Author: Tony DiCola
# License: Public Domain
import sys
import time
from influxdb import InfluxDBClient
import RPi.GPIO as GPIO 

# Raspberry setup
pin = 4
GPIO.setmode(GPIO.BCM) 

# Import the ADS1x15 module.
import Adafruit_ADS1x15

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('giessen')

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Or create an ADS1015 ADC (12-bit) instance.
#adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

# Start continuous ADC conversions on channel 0 using the previously set gain
# value.  Note you can also pass an optional data_rate parameter, see the simpletest.py
# example and read_adc function for more infromation.
adc.start_adc(0, gain=GAIN)
# Once continuous ADC conversions are started you can call get_last_result() to
# retrieve the latest result, or stop_adc() to stop conversions.

# Note you can also call start_adc_difference() to take continuous differential
# readings.  See the read_adc_difference() function in differential.py for more
# information and parameter description.

# Read channel 0 for 5 seconds and print out its values.
if (len(sys.argv)==2 and sys.argv[1]=="inf"):
    print(time.asctime(time.localtime(time.time())))
    print('Reading ADS1x15 channel 0 for 5 seconds...')
    while True:
        value = adc.get_last_result()
        print('Channel 0: {0}'.format(value))
        time.sleep(0.5)
else:
    raw_values=[]
    for i in range(6): # 0 to 5
        value = adc.get_last_result()
        raw_values.append(value)
        time.sleep(0.5)
    json_data = [
            {
            "measurement": "feuchte",
            "fields": {
                "location": "bonsai1",
                "value": raw_values[3], # use median (3rd value)
            },
            "time": time.asctime(time.localtime(time.time()))
            }
    ]
    client.write_points(json_data)
    if raw_values[3] > 16500:
        try:
            GPIO.setup(pin, GPIO.OUT) 
            time.sleep(3) 
            GPIO.setup(pin, GPIO.IN) 
        except:
            GPIO.setup(pin, GPIO.IN) 
            GPIO.cleanup()

# Stop continuous conversion.  After this point you can't get data from get_last_result!
adc.stop_adc()
