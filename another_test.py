import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

dout_pin = 5 #GPIO pin number
pd_sck_pin = 6
hx = HX711(dout_pin, pd_sck_pin)
hx.zero()

#the lower the readings parameter the faster it reads the stuff 
while True:
    
    reading = hx.get_data_mean(readings=2)
    print(reading)
