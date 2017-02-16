#!/usr/bin/python
from dronekit import connect
import sys
from time import sleep

def dump_value_callback(self, attr_name, value):
        print "{0}: {1}".format(attr_name, value)

target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print 'Connecting to ' + target + '...'
vehicle = connect(target, wait_ready=True)

print "Registering listeners"

vehicle.add_attribute_listener('*', dump_value_callback)

print "Entering wait loop"
while True:
        print "Waiting..."
        sleep(60)

vehicle.close()

print "Done."



