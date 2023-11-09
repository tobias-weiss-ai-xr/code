import smbus2
import bme280

# Create library object using our Extended Bus I2C port
port = 0
address = 0x76
bus = smbus2.SMBus(port)

#Get bme data
calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)

print("\nTemperature: %0.1f C" % data.temperature)
