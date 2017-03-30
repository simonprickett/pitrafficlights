import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

while True:
	GPIO.output(9, True)
	time.sleep(3)
	GPIO.output(10, True)
	time.sleep(1)
	GPIO.output(9, False)
	GPIO.output(10, False)
	GPIO.output(11, True)
	time.sleep(5)
	GPIO.output(11, False)
	GPIO.output(10, True)
	time.sleep(2)
	GPIO.output(10, False)