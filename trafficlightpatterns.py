import RPi.GPIO as GPIO
import time
import os

pattern = os.environ['TRAFFIC_LIGHT_COUNTRY']
pattern = pattern.lower()

print pattern

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

# Loop forever
while True:
	# Red
	GPIO.output(9, True)
	time.sleep(3)
	# Red and amber
	GPIO.output(10, True)
	time.sleep(1)
	# Green
	GPIO.output(9, False)
	GPIO.output(10, False)
	GPIO.output(11, True)
	time.sleep(5)
	# Amber
	GPIO.output(11, False)
	GPIO.output(10, True)
	time.sleep(2)
	# Amber off (red comes on at top of loop)
	GPIO.output(10, False)