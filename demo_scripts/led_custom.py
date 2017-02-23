#!/usr/bin/python
from dronekit import connect
import sys
from time import sleep
from SoloLED import SoloLED
 
target = 'udpin:0.0.0.0:14550'
print 'Connecting to ' + target + '...'
vehicle = connect(target, wait_ready=True)

SoloLED.custom(vehicle, 0, [SoloLED.PATTERN_SOLID, SoloLED.PARAM_BIAS_RED, 0, SoloLED.PARAM_BIAS_GREEN, 0, SoloLED.PARAM_BIAS_BLUE, 255])

vehicle.flush()

sleep(30)

# Reset LED's to default / vehicle controlled mode
SoloLED.macro(vehicle, SoloLED.LED_ALL, SoloLED.MACRO_RESET)

vehicle.close()
print "Done."



