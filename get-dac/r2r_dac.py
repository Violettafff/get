<<<<<<< HEAD
import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):        
        GPIO.output(self.gpio_bits, [int(element) for element in bin(number)[2:].zfill(8)])
              
        if self.verbose:
            print(f"Выведено число: {number}")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за ДД ЦАП (0.00-{self.dynamic_range:.2f}) В")
            print("Устанавливаем 0.0В")
            self.set_number(0)
        else:
            number = int((voltage / self.dynamic_range) * 255)
            self.set_number(number)


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()
=======
import RPIO.GPIO as GPIO
class R2R_DAC:
    def _init_(self,gpio_bits,dynamic_range,verbose=False):
       self.gpio_bits=gpio.bits
       self.dynamic_range=dynamic_range
       self.verbose=verbose
       GPIO.setmode(GPIO.BCM)
       GPIO.setup(self.gpio_bits,GPIO.OUT,initial=0)
    def deinit(self):
        GPIO.output(self.gpio_bits,0)
        GPIO.cleanup()
    def set_number(self,number):
        binary_string=bin(number)[2:].zfill(8)
        bits=[int(bit) for bit in binary_string]
        for pin, bit in zip(self.gpio_bits,bits):
            GPIO.output(pin,bit)
        if self.verbose:
            print(f"Число на вход ЦАП:{number}",биты:{bits}")
    def set_voltage(self,voltage):
        if not(0.0<=voltage<=self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон")
            self.set_number(0)
            return
        number=int(voltage/self.dynamic_range*255)
        self.set_number(number)

if _name_ =="_main_":
    try:
        dac=R2R_DAC([16,20,21,25,26,17,27,22])
        while True:
            try:
                voltage=float(input("Введите напряжение:"))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число")
    finally:
        dac.deinit()
>>>>>>> 2c8f68b9feac98e28b11d7da0d8643abec0c6c86
