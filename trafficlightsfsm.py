#import RPi.GPIO as GPIO
import time
import os
import signal
import sys

#TODO Should each state set all 3 lights so it could be started in any state?

class TrafficLightStates:
	INITIALIZING = 1
	RED = 2
	REDAMBER = 3
	GREEN = 4
	AMBER = 5

currentState = TrafficLightStates.INITIALIZING

while True:
	if (currentState == TrafficLightStates.INITIALIZING):
		print 'Initializing'

		if ('TRAFFIC_LIGHT_COUNTRY' in os.environ) and (os.environ['TRAFFIC_LIGHT_COUNTRY'] in ['UK', 'USA']):
			pattern = os.environ['TRAFFIC_LIGHT_COUNTRY'].lower()
		else:
			print('TRAFFIC_LIGHT_COUNTRY should be set to UK or USA')
			sys.exit(1)

		# Setup Hardware
		#GPIO.setmode(GPIO.BCM)
		#GPIO.setup(9, GPIO.OUT)
		#GPIO.setup(10, GPIO.OUT)
		#GPIO.setup(11, GPIO.OUT)

		currentState = TrafficLightStates.RED

	elif (currentState == TrafficLightStates.RED):
		print 'Red'
		#GPIO.output(9, True)
		time.sleep(3)

		if pattern == 'uk':
			currentState = TrafficLightStates.REDAMBER
		else:
			currentState = TrafficLightStates.GREEN

	elif (currentState == TrafficLightStates.REDAMBER):
		print 'RedAmber'
		#GPIO.output(10, True)
		time.sleep(1)

		currentState = TrafficLightStates.GREEN

	elif (currentState == TrafficLightStates.GREEN):
		print 'Green'
		#GPIO.output(9, False)
		#GPIO.output(10, False)
		#GPIO.output(11, True)
		time.sleep(5)
		
		currentState = TrafficLightStates.AMBER

	elif (currentState == TrafficLightStates.AMBER):
		print 'Amber'
		#GPIO.output(11, False)
		#GPIO.output(10, True)
		
		if pattern == 'uk':
			# Short wait
			time.sleep(2)
		else:
			# Longer wait
			time.sleep(3)

		currentState = TrafficLightStates.RED
	else:
		print 'Invalid state!'

# Turn off all lights when user ends demo
def allLightsOff(signal, frame):
	#GPIO.output(9, False)
	#GPIO.output(10, False)
	#GPIO.output(11, False)
	#GPIO.cleanup()
	print "PI SIM All lights off"
	sys.exit(0)

signal.signal(signal.SIGINT, allLightsOff)

# Loop forever
while True:
	# Red
	print "PI SIM Red on"
	#GPIO.output(9, True)
	time.sleep(3)
	
	# Red and amber for UK only
	if (pattern == 'uk'):
		print "PI SIM Red and amber on"
		#GPIO.output(10, True)

	time.sleep(1)

	# Green
	print "PI SIM Green on"
	#GPIO.output(9, False)
	#GPIO.output(10, False)
	#GPIO.output(11, True)
	time.sleep(5)
	
	# Amber, longer in US than UK
	print "PI SIM Amber on"
	#GPIO.output(11, False)
	#GPIO.output(10, True)
	if (pattern == 'uk'):
		time.sleep(2)
	else:
		time.sleep(3)
	
	# Amber off (red comes on at top of loop)
	print "PI SIM Amber off"
	#GPIO.output(10, False)