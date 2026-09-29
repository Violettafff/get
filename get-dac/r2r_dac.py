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
