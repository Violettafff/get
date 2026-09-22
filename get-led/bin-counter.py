import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds=[24,22,23,27,17,25,12,16]
GPIO.setup(leds,GPIO.OUT)
GPIO.output(leds,0)
Up=9
Down=10
GPIO.setup(Up,GPIO.IN)
GPIO.setup(Down,GPIO.IN)
num=0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleeptime=0.1
while True:
    if GPIO.input(Up):
        num+=1
        if num>255:
            num=0
        time.sleep(sleeptime)
    if GPIO.input(Down):
        num-=1
        if num<0:
            num=0
        time.sleep(sleeptime)
    GPIO.output(leds,dec2bin(num))