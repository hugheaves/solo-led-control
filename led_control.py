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

 
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help', dest="command")
resetParser = subparsers.add_parser('reset', help="Reset LED to default (system controlled) state")
resetParser.add_argument("led", metavar="led", choices=["all", "front_left", "front_right", "back_left", "back_right"], help="LED selection, one of: %(choices)s")
colorParser = subparsers.add_parser('color', help='Set LED to a fixed color and pattern')
colorParser.add_argument("led", metavar="led", choices=["all", "front_left", "front_right", "back_left", "back_right"], help="LED selection, one of: %(choices)s")
colorParser.add_argument("pattern",  metavar="flash pattern", choices=["sine", "solid", "siren", "strobe", "fadein", "fadeout"], help="LED flash pattern, one of: %(choices)s")
colorParser.add_argument("red", type=int, metavar="red", help="red brightness value (0 <= value <= 255)",choices=xrange(0,256))
colorParser.add_argument("green", type=int, metavar="green", help="green brightness value (0 <= value <= 255)",choices=xrange(0,256))
colorParser.add_argument("blue", type=int, metavar="blue", help="blue brightness value (0 <= value <= 255)",choices=xrange(0,256))

args = parser.parse_args()

soloLED = SoloLED('udpin:127.0.0.1:14550', wait_ready=False)

led = getattr(SoloLED, "LED_" + args.led.upper())

if args.command == 'reset':
    print "Resetting to default colors / vehicle controlled mode"
    soloLED.macro(led, SoloLED.MACRO_RESET)
elif args.command == 'color':
    print "Setting pattern / color"
    soloLED.rgb(led, getattr(SoloLED, "PATTERN_" + args.pattern.upper()), args.red, args.green, args.blue)
        
    
soloLED.close()
print "Done."
