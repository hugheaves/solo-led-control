#!/usr/bin/python
from dronekit import connect
import sys
from time import sleep
import SoloLED

def attitude_callback(self, attr_name, attitude):
        print "Attitude: {0}".format(attitude)
        back_left = -attitude.roll + attitude.pitch
        back_right = attitude.roll + attitude.pitch
        front_left = -attitude.roll - attitude.pitch
        front_right = attitude.roll - attitude.pitch
        print "back_left: {0} back_right {1} front_left {2} front_right {3}".format(back_left, back_right, front_left, front_right)
        SoloLED.setLEDRGB(vehicle, SoloLED.LED_BACK_LEFT, SoloLED.PATTERN_SOLID, red_val(back_left), green_val(back_left), 0)
        SoloLED.setLEDRGB(vehicle, SoloLED.LED_BACK_RIGHT, SoloLED.PATTERN_SOLID, red_val(back_right), green_val(back_right), 0)
        SoloLED.setLEDRGB(vehicle, SoloLED.LED_FRONT_LEFT, SoloLED.PATTERN_SOLID, red_val(front_left), green_val(front_left), 0)
        SoloLED.setLEDRGB(vehicle, SoloLED.LED_FRONT_RIGHT, SoloLED.PATTERN_SOLID, red_val(front_right), green_val(front_right), 0)
        vehicle.flush()

def red_val(raw_value):
        scaled = int(raw_value * 128 + 127)
        if (scaled < 0):
                scaled = 0
        if (scaled > 255):
                scaled = 255
        return scaled

def green_val(raw_value):
        return 255 - red_val(raw_value)

 
target = 'udpin:0.0.0.0:14550'
print 'Connecting to ' + target + '...'
vehicle = connect(target, wait_ready=True)

print "Registering listeners"
vehicle.add_attribute_listener('attitude', attitude_callback)

print "Waiting..."
sleep(120)

vehicle.close()

print "Done."



