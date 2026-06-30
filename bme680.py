#On Raspberry Pi desktop -> pip install bme680

import time
import bme680
from datetime import datetime

try:
  sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
  # Connects the sensor using standard factory digital address, connection under variable named sensor
except (RuntimeError, IOError):
  sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
# if hardware chip was manufactured with a different internal address, connects to backup digital address

# Oversampling for best accuracy, samples x times and averages out
sensor.set_humidity_oversampling(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversampling(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
# turns on internal hardware filter to smooth out unrealistic spikes in data

print("BME680 Radiative Cooling Data Logger Started")
print("Press Ctrl+C to stop recording.")

# Data loop
try:
  while True:
    # Check if new reading available
    if sensor.get_sensor_data():
      # get current timestamp
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      # extract properties from chip
      temperature_c = sensor.data.temperature
      humidity_rh = sensor.data.humidity
      pressure_hpa = sensor.data.pressure
      #f string -> treat as text except in curly brackets, grab variable value and put in text
      print(f"[{timestamp}] Temperature: {temperature_c:.2f} °C | Humidity: {humidity_rh:.2f} % | Pressure: {pressure_hpa:.2f} hPa")
      # look at specific variables, prints in square brackets, .2f so it rounds to two decimal places
    time.sleep(10)
    #Wait 10 seconds before requesting next datapoint
#But if ctrl+C is pressed
except KeyboardInterrupt:
  print("Data logging stopped")
  

      
