import Adafruit_DHT
import time
from rpi_lcd import LCD

lcd = LCD()
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        lcd.text("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidi>
    time.sleep(1.5);
