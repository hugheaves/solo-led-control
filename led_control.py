#!/usr/bin/python
'''
  Copyright (C) 2017  Hugh Eaves
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
 
  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import argparse
from SoloLED import SoloLED

class AppendAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not namespace.commands:
            namespace.commands = [];
        optionName = option_string.lstrip(parser.prefix_chars)
        valueList = getattr(namespace, self.dest)
        if not valueList:
            valueList = []
            setattr(namespace, self.dest, valueList)
        if not self.const:
            valueList.append((optionName , values))
        else:
            valueList.append((optionName , values))
        return

def toLED(led):
    return getattr(SoloLED, "LED_" + led.upper())

def toPattern(pattern):
    return getattr(SoloLED, "PATTERN_" + pattern.upper())

parser = argparse.ArgumentParser()
parser.add_argument("--reset", action=AppendAction, dest="commands", const=True, nargs=0, help="Reset to default color and pattern.")
parser.add_argument("--pattern", action=AppendAction, dest="commands", choices=["sine", "solid", "siren", "strobe", "fadein", "fadeout"], help="Set LED flash pattern.")
parser.add_argument("--color", action=AppendAction, dest="commands", nargs=3, metavar=("red", "green", "blue"), type=int, choices=range(0, 256), help="Set LED red, green, and blue brightness values. (range 0 - 255)")
parser.add_argument("--applyto", action=AppendAction, required=True, dest="commands", choices=["all", "front_left", "front_right", "back_left", "back_right"], help="Apply settings to LED(s)")
parser.add_argument("--ip", metavar = "protocol:ipAddress:port", default="udpin:127.0.0.1:14550", help = "Protocol / IP address / Port number for connction")

parsedArgs = parser.parse_args()

soloLED = SoloLED(parsedArgs.ip);

state = None
color = [255, 255, 255]
pattern = SoloLED.PATTERN_SOLID

for command in parsedArgs.commands:
    commandName = command[0]
    commandArgs = command[1]
    if (commandName == "applyto"):
        if (state == None):
            raise Exception, "No settings to apply"
        elif (state == "pattern" or state == "color"):
            soloLED.color(toLED(commandArgs), pattern, color[0], color[1], color[2]) 
        elif (state == "reset"):
            soloLED.reset(toLED(commandArgs))
        else:
            raise Exception, "Unknown state"
    elif (commandName == "pattern"):
        state = commandName
        pattern = toPattern(commandArgs)
    elif (commandName == "color"):
        state = commandName
        color = commandArgs
    elif (commandName == "reset"):
        state = commandName
    else:
        raise ValueError, "Unrecognized command name " + commandName

#sleep(10)

soloLED.close()
print "Done."
