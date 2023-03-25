import RPi.GPIO as GPIO

from hx711 import HX711
import pickle as pkl


class LoadCellHX711():
    def __init__(self, dout_pin:int, pd_sck_pin:int) -> None:
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self.hx = HX711(self.dout_pin, self.pd_sck_pin)

    def zero_out_readings(self) -> None:
        self.hx.zero()
        print("zeroed out")

    def get_filtered_data(self,reading_sample:int) -> float:
        return self.hx.get_data_mean(reading_sample)    

    def calibrate_sensor(self, reading_sample=100) -> None:
        input('Place known weight on scale and press Enter: ')
        reading = self.get_filtered_data(reading_sample)

        known_weight_grams = input('Enter the known weight in grams and press Enter: ')
        float_grams = float(known_weight_grams)
        ratio = reading/float_grams
        self.hx.set_scale_ratio(ratio)

        print("Calibrated!")
        return 

    def load_ratio(self):
        input ('Do you want to load your calibration information? (y/n): ')
        if input == 'y':
            with open('calibration.pkl', 'rb') as f:
                self.hx.set_scale_ratio(pkl.load(f))
            print("Loaded!")
            return
        else:
            print("Not loaded!")
            return

    def save_ratio(self):
        input('Do you want to save your calibration information? (y/n): ')
        if input == 'y':
            with open('calibration.pkl', 'wb') as f:
                pkl.dump(self.hx.get_scale_ratio(), f)
            print("Saved!")
        else:
            print("Not saved!")
        return
    
def init_gpio() -> None:
    GPIO.setmode(GPIO.BCM)
    print("set mode GPIO")
    return

def convert_grams_to_lbs(gram_val:float) -> float:
    return gram_val * 0.00220462

if __name__=='__main__':
    init_gpio()
    dout_pin = 5 #GPIO pin number
    pd_sck_pin = 6
    hx = LoadCellHX711(dout_pin, pd_sck_pin)
    hx.zero_out_readings()

    hx.calibrate_sensor()

    try:
        while True:
            readings = hx.get_filtered_data(5)
            print(convert_grams_to_lbs(readings))

    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

    finally:
        GPIO.cleanup()


