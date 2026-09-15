import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led=26
GPIO.setup(led,GPIO.OUT)
light=6
GPIO.setup(light,GPIO.IN)
while True:
    state=GPIO.input(light)
    GPIO.output(led,not state)