from machine import Pin, ADC
import utime as time
from dht11 import DHT11


sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)



while True:
    time.sleep(5)
    reading = sensor_temp.read_u16() * conversion_factor
    
    temperature = 27 - (reading - 0.706)/0.001721
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature:{}".format(t))
    print("Temperature2:{}".format(temperature))
    print("Humidity:{}".format(h))
    
