# Measures Temperature, Humidity, Pressure
# BME280 - Adafruit

import time

#from Adafruit_BME280 import *

import board

from adafruit_bme280 import basic as adafruit_bme280


#sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode = BME280_OSAMPLE_8)

i2c = board.I2C()
sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c)

times = []
temperatures = []

start_time = time.time()
run_time = 10
stop_time = start_time + run_time
current_time = time.time()
while current_time < stop_time:
	current_time = time.time()
	temp = sensor.temperature
	humidity = sensor.relative_humidity
	pressure = sensor.pressure
	print(temp)
	times.append(current_time)
	temperatures.append(temp)
	time.sleep(1)
	
print(temperatures)
