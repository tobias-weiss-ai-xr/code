import smbus2
import bme280
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

port = 0
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# there is a handy string representation too
for item in data:
    print(item)
