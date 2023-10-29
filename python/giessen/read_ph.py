import time
import board
import busio
import numpy as np
import adafruit_ads1x15.ads1015 as ADS
import influxdb_client
from adafruit_ads1x15.analog_in import AnalogIn
from influxdb_client.client.write_api import SYNCHRONOUS

# influx config
org = "giessen"
token = "_nBhhHy_CuVXPU6SM6017SrVaNaG6KQXDEFnUIDFpJPGvlCo7P5eXRnUZhCbfpKmAWIIpss39B5Rgj9lLPY--g=="
url="http://192.168.1.1:8086"


# ph
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0)
# measurements
vals = []
for i in range(3):
    vals.append(chan.value)
    print(chan.voltage, chan.value)
    mean = np.mean(vals)
    time.sleep(1)

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("ph").tag("location", "giessen").field("ph", mean)
write_api.write(bucket="ph", org=org, record=p)

print(f"ph measure {mean} saved! {mean*(5/1024)}")
