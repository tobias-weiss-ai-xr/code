import adafruit_ads1x15.ads1015 as ADS
import bme280
import board
import busio
import influxdb_client
import json
import smbus2
import time
import numpy as np
from adafruit_ads1x15.analog_in import AnalogIn
from influxdb_client.client.write_api import SYNCHRONOUS

# influx config
org = "giessen"
token = "_nBhhHy_CuVXPU6SM6017SrVaNaG6KQXDEFnUIDFpJPGvlCo7P5eXRnUZhCbfpKmAWIIpss39B5Rgj9lLPY--g=="
url="http://192.168.1.1:8086"

while True: 
    # measurements
    vals = []

    # bme280
    port = 0
    address = 0x76
    bus = smbus2.SMBus(port)
    calibration_params = bme280.load_calibration_params(bus, address)
    temp = []
    pres = []
    humi = []
    for j in range(5):
        val = bme280.sample(bus, address, calibration_params)
        temp.append(val.temperature)
        pres.append(val.pressure)
        humi.append(val.humidity)

    temp = np.sort(temp)
    pres = np.sort(pres)
    humi = np.sort(humi)
        
    # cap
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1015(i2c)
    channels = [AnalogIn(ads, ADS.P1), AnalogIn(ads, ADS.P2), AnalogIn(ads, ADS.P3)]
    for i, chan in enumerate(channels):
        tmp = []
        for j in range(5):
           tmp.append(chan.value)

        tmp = np.sort(tmp)
        vals.append((f"cap{i}", tmp[2]))

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    # Write script
    write_api = client.write_api(write_options=SYNCHRONOUS)
    # the compensated_reading class has the following attributes
    vals += [("temp", temp[2]), ("pressure", pres[2]), ("hum", humi[2])]

    for key, val in vals:
        print(key, val)
        time.sleep(3)
