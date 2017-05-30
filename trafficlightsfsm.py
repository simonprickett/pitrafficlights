import RPi.GPIO as GPIO
import time
import os
import signal
import sys

class TrafficLightLEDs:
	RED = 9
	AMBER = 10
	GREEN = 11

class TrafficLightStates:
	INITIALIZING = 1
	RED = 2
	REDAMBER = 3
	GREEN = 4
	AMBER = 5

# Turn off all lights when user ends demo
def allLightsOff(signal, frame):
	GPIO.output(TrafficLightLEDs.RED, False)
	GPIO.output(TrafficLightLEDs.AMBER, False)
	GPIO.output(TrafficLightLEDs.GREEN, False)
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, allLightsOff)

currentState = TrafficLightStates.INITIALIZING

while True:
	if (currentState == TrafficLightStates.INITIALIZING):
		if ('TRAFFIC_LIGHT_COUNTRY' in os.environ) and (os.environ['TRAFFIC_LIGHT_COUNTRY'] in ['UK', 'USA']):
			pattern = os.environ['TRAFFIC_LIGHT_COUNTRY'].lower()
		else:
			print('TRAFFIC_LIGHT_COUNTRY should be set to UK or USA')
			sys.exit(1)

		# Setup Hardware
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(TrafficLightLEDs.RED, GPIO.OUT)
		GPIO.setup(TrafficLightLEDs.AMBER, GPIO.OUT)
		GPIO.setup(TrafficLightLEDs.GREEN, GPIO.OUT)

		currentState = TrafficLightStates.RED

	elif (currentState == TrafficLightStates.RED):
		GPIO.output(TrafficLightLEDs.RED, True)
		GPIO.output(TrafficLightLEDs.AMBER, False)
		GPIO.output(TrafficLightLEDs.GREEN, False)
		time.sleep(3)

		if pattern == 'uk':
			currentState = TrafficLightStates.REDAMBER
		else:
			currentState = TrafficLightStates.GREEN

	elif (currentState == TrafficLightStates.REDAMBER):
		GPIO.output(TrafficLightLEDs.RED, True)
		GPIO.output(TrafficLightLEDs.AMBER, True)
		GPIO.output(TrafficLightLEDs.GREEN, False)
		time.sleep(1)

		currentState = TrafficLightStates.GREEN

	elif (currentState == TrafficLightStates.GREEN):
		GPIO.output(TrafficLightLEDs.RED, False)
		GPIO.output(TrafficLightLEDs.AMBER, False)
		GPIO.output(TrafficLightLEDs.GREEN, True)
		time.sleep(5)
		
		currentState = TrafficLightStates.AMBER

	elif (currentState == TrafficLightStates.AMBER):
		GPIO.output(TrafficLightLEDs.RED, False)
		GPIO.output(TrafficLightLEDs.AMBER, True)
		GPIO.output(TrafficLightLEDs.GREEN, False)
		
		if pattern == 'uk':
			# Short wait
			time.sleep(2)
		else:
			# Longer wait
			time.sleep(3)

		currentState = TrafficLightStates.RED
	else:
		print 'Invalid state!'
