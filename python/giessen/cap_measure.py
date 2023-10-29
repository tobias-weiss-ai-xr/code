import time
import json
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)
# Create single-ended input on channel 0
channels = [AnalogIn(ads, ADS.P0), AnalogIn(ads, ADS.P1)]


with open("cap_config.json") as json_data_file:
    config_data = json.load(json_data_file)
# print(json.dumps(config_data))

def percent_translation(raw_val):
    per_val = abs((raw_val- config_data["zero_saturation"])/(config_data["full_saturation"]-config_data["zero_saturation"]))*100
    return round(per_val, 3)

if __name__ == '__main__':
    print("----------  {:>5}\t{:>5}".format("Saturation", "Voltage\n"))
    while True:
        try:
            for chan in channels:
                print("SOIL SENSOR: " + "{:>5} {:>5}%\t{:>5.3f}".format(chan.value, percent_translation(chan.value), chan.voltage))
        except Exception as error:
            raise error
        except KeyboardInterrupt:
            print('exiting script')
        time.sleep(1)
