import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]   # MSB первый, bit6 = GPIO12
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

Up = 9
Down = 10
GPIO.setup(Up, GPIO.IN)
GPIO.setup(Down, GPIO.IN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    up_pressed   = GPIO.input(Up)
    down_pressed = GPIO.input(Down)

    if up_pressed and down_pressed:
        # одновременное нажатие — устанавливаем максимум
        num = 255
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    elif up_pressed:
        num += 1
        if num > 255:
            num = 0
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    elif down_pressed:
        num -= 1
        if num < 0:
            num = 0
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    GPIO.output(leds, dec2bin(num))
