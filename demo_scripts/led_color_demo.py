#!/usr/bin/python

from time import sleep
from SoloLED import SoloLED
 
soloLED = SoloLED()

soloLED.rgb(SoloLED.LED_BACK_RIGHT, SoloLED.PATTERN_SOLID, 0, 0, 255)
soloLED.rgb(SoloLED.LED_BACK_LEFT, SoloLED.PATTERN_SOLID, 0, 255, 0)
soloLED.rgb(SoloLED.LED_FRONT_RIGHT, SoloLED.PATTERN_SOLID, 255, 0, 0)
soloLED.rgb(SoloLED.LED_FRONT_LEFT, SoloLED.PATTERN_SOLID, 255, 50, 0)

print "Sleeping for 30 seconds..."
sleep(30)

print "Resetting LED's to default colors / vehicle controlled mode"
SoloLED.macro(SoloLED.LED_ALL, SoloLED.MACRO_RESET)

soloLED.close()

print "Done."



