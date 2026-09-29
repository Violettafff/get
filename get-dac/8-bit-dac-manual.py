import RPi.GPIO as GPIO
dac_bits=[16,20,21,25,26,17,27,22]
dynamic_range=3.3
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits,GPIO.OUT)
def voltage_to_number(voltage):
    if not(0.0<=voltage<=dynamic_range):
        print(f"Напряжение выходит за диапазон(0.00-{dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 В")
        return 0
    return int (voltage/dynamic_range*255) 
def number_to_dac(number):
    binary_string=bin(number)[2::].zfill(8)
    bits=[int(bit) for bit in binary_string] 
    for pin, bit in zip(dac_bits, bits):
        GPIO.output(pin,bit) 
    print(f"Число ан входе:{number},биты:{bits}")     
try:
    while True:
        try:
            voltage=float(input("Введите напряжение в Вольтах: "))
            number=voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Вы не ввели число")        
finally:
    GPIO.output(dac_bits,0)
    GPIO.cleanup()

