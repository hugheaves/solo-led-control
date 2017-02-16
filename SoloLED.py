#!/usr/bin/python

# LED positions for all setLED functions
LED_BACK_LEFT = 0
LED_BACK_RIGHT = 1
LED_FRONT_RIGHT = 2
LED_FRONT_LEFT = 3
LED_ALL = 255

# Macros for setLEDMacro function
MACRO_RESET = 0 # Removes LED color override
MACRO_COLOUR_CYCLE = 1 # Party colors
MACRO_BREATH = 2 # Adds a on/off cycle to any mode
MACRO_STROBE = 3 # Turn LED's off
MACRO_FADEIN = 4 # No-Op
MACRO_FADEOUT = 5 # No-Op
MACRO_RED = 6 # No-Op
MACRO_GREEN = 7 # No-Op
MACRO_BLUE = 8 # No-Op
MACRO_YELLOW = 9 # All yellow
MACRO_WHITE = 10 # All LED's white
MACRO_AUTOMOBILE = 11 # White in front, red in back
MACRO_AVIATION = 12 # White / red / green

# Commands for setLEDCustom function
PARAM_BIAS_RED = 0
PARAM_BIAS_GREEN = 1
PARAM_BIAS_BLUE = 2
PARAM_AMPLITUDE_RED = 3
PARAM_AMPLITUDE_GREEN = 4
PARAM_AMPLITUDE_BLUE = 5
PARAM_PERIOD = 6
PARAM_REPEAT = 7
PARAM_PHASEOFFSET = 8
PARAM_MACRO = 9
PARAM_RESET = 10
PARAM_APP_CHECKSUM = 11 # Not sure what this does.

# Patterns for setLEDRGB function
PATTERN_OFF = 0
PATTERN_SINE = 1
PATTERN_SOLID = 2
PATTERN_SIREN = 3
PATTERN_STROBE = 4
PATTERN_FADEIN = 5
PATTERN_FADEOUT = 6
PATTERN_PARAMUPDATE = 7  # Not sure what this does.

# Set LED macro
def setLEDMacro(vehicle, led, macro):
        byteArray = bytearray()
        padByteArray(byteArray)
        msg = vehicle.message_factory.led_control_encode(0, 0, led, macro, 0, byteArray)
        vehicle.send_mavlink(msg)

# Set LED pattern and color (RGB value)
def setLEDRGB(vehicle, led, pattern, red, green, blue):
        byteArray = bytearray(['R', 'G', 'B', '0', pattern, red, green, blue])
        padByteArray(byteArray)
        msg = vehicle.message_factory.led_control_encode(0, 0, led, 255, 8, byteArray)
        vehicle.send_mavlink(msg)
 
# Set a custom mode / message for a LED
def setLEDCustom(vehicle, led, customBytes):
        byteArray = bytearray(['C', 'M', 'D', '0'])
	byteArray.extend(bytearray(customBytes))
	print byteArray
	arrayLength = len(byteArray)
	padByteArray(byteArray)
	print byteArray
        msg = vehicle.message_factory.led_control_encode(0, 0, led, 255, arrayLength, byteArray)
        vehicle.send_mavlink(msg)

# Pad byteArray to required length for custom message (24 bytes)
def padByteArray(byteArray):
	byteArray += bytearray([0]) * (24 - len(byteArray))	



