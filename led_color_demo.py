#!/usr/bin/python
from dronekit import connect
import sys
from time import sleep
import SoloLED
 
target = 'udpin:0.0.0.0:14550'
print 'Connecting to ' + target + '...'
vehicle = connect(target, wait_ready=True)

SoloLED.setLEDRGB(vehicle, SoloLED.LED_BACK_RIGHT, SoloLED.PATTERN_SOLID, 0, 0, 255)
SoloLED.setLEDRGB(vehicle, SoloLED.LED_BACK_LEFT, SoloLED.PATTERN_SOLID, 0, 255, 0)
SoloLED.setLEDRGB(vehicle, SoloLED.LED_FRONT_RIGHT, SoloLED.PATTERN_SOLID, 255, 0, 0)
SoloLED.setLEDRGB(vehicle, SoloLED.LED_FRONT_LEFT, SoloLED.PATTERN_SOLID, 255, 50, 0)

vehicle.flush()

sleep(30)

# Reset LED's to default / vehicle controlled mode
SoloLED.setLEDMacro(vehicle, SoloLED.LED_ALL, SoloLED.MACRO_RESET)

vehicle.close()
print "Done."



