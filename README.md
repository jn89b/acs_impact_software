# ACS Impact Software
This repo contains the software for impact testing for UMKC's Aircraft Combat Surviability class. It interfaces with a Raspberry pi and HX711 amplifier to read measurements from the impact of a load cell 

# Requirements
This repo requires the https://github.com/gandalf15/HX711 repo to interact with the load cell to install do the following:

```
pip3 install 'git+https://github.com/gandalf15/HX711.git#egg=HX711&subdirectory=HX711_Python3'
```

# Important notes
To read data faster set the reading to 1, it is set at 30 as default
```python
import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

dout_pin = 5 #GPIO pin number
pd_sck_pin = 6
hx = HX711(dout_pin, pd_sck_pin)
#zero out the values
hx.zero()


#the lower the readings parameter the faster it reads the stuff 
while True:
    #this line of code gets the raw data mean
    #reading = hx.get_raw_data_mean(readings=1)

    #this line gets the filtered data
    reading = hx.get_data_mean()

    print(reading)

```