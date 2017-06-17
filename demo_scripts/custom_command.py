#!/usr/bin/python

from time import sleep
from SoloLED import SoloLED
 
soloLED = SoloLED()

print "Sending second command"
soloLED.custom(SoloLED.LED_FRONT_RIGHT, [SoloLED.PATTERN_PARAMUPDATE, SoloLED.PARAM_PERIOD, 30])
soloLED.custom(SoloLED.LED_FRONT_RIGHT, [SoloLED.PATTERN_PARAMUPDATE, SoloLED.PARAM_PHASEOFFSET, 10])
soloLED.custom(SoloLED.LED_FRONT_RIGHT, [SoloLED.PATTERN_PARAMUPDATE, SoloLED.PARAM_BIAS_RED, 127])
soloLED.custom(SoloLED.LED_FRONT_RIGHT, [SoloLED.PATTERN_PARAMUPDATE, SoloLED.PARAM_AMPLITUDE_RED, 32])
soloLED.custom(SoloLED.LED_FRONT_RIGHT, [SoloLED.PATTERN_SINE, SoloLED.PARAM_BIAS_RED, 255, SoloLED.PARAM_BIAS_GREEN, 255, SoloLED.PARAM_BIAS_BLUE, 255,
                                         SoloLED.PATTERN_PARAMUPDATE, SoloLED.PARAM_PERIOD, 30])


print "Sleeping for 10 seconds..."
sleep(10)

print "Resetting LED's to default colors / vehicle controlled mode"
soloLED.macro(SoloLED.LED_ALL, SoloLED.MACRO_RESET)

soloLED.close()

print "Done."



