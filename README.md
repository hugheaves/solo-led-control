# Disclaimer
Gaining full control of the LED's on your 3DR Solo requires installing non-factory / unsupported software on your 3DR Solo. **Doing so will almost certainly void your warranty, and could cause irreparable damage to your Solo or other property, personal injury, or even loss of life. Proceed with caution**.

Therefore, from the GPL, under which this software is licensed:

> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# Installation
To control the color and/or illumination pattern of the 3DR Solo LEDs you must install modified PixHawk firmware and several files from this repository. The following instructions are written assuming some degree of expertise with this process.


## Firmware Installation
* Download the lastest release of "ArduCopter-v2.px4" from [https://github.com/hugheaves/ardupilot-solo/releases](https://github.com/hugheaves/ardupilot-solo/releases)

* Install the firmware on your Solo using the standard PixHawk firmware upgrade procedure described here:
[https://www.github.com/3drobotics/ardupilot-solo](https://www.github.com/3drobotics/ardupilot-solo)

* Verify that the correct firmware is installed by connecting to your Solo with Solex or a similar application (e.g. Solo or Tower). Use the application to check the version of the flight controller firmware. If the custom firmware is correctly installed, the app will show the flight  version as "93.7.xxx" where "93.7.xxx" matches the version that you downloaded from the releases page.

## Script Installation
Once you have the firmware installed, copy the required scripts from this repository to your Solo:

* Using the same file transfer software you used for the firmware, copy *SoloLED.py* and *led_control.py* from this repository to your Solo. You can place the scripts anywhere you want, but the easiest location is directly in the root home directory (/root). This directory is included in the system default PATH and will allow you to easily run and update the scripts.

**Note:** The other files, such as those in the demo_scripts directory, are not necessary for basic control of the LEDs.

# Usage
Once everything is installed, you can run the "led_control.py" script to control the LEDs on Solo. You can run the script using Solex's "command" feature, or via an interactive SSH connection.

The command to run the script is:

`python led_control.py`

Depending on where and how you uploaded the script, you may also be able to run the script directly, like this:

`led_control.py`

For simplicity, all the examples here assume the latter method. With either method, commands are added at the end of the command line (after led_control.py) to specify the control actions.

Running the script with the "-h" option will display usage information:

`led_control.py -h`

~~~~~
usage: led_control.py [-h] [--reset]
               [--pattern {sine,solid,siren,strobe,fadein,fadeout}]
               [--color red green blue] --applyto
               {all,front_left,front_right,back_left,back_right}
               [--ip protocol:ipAddress:port]

optional arguments:
  -h, --help            show this help message and exit
  --reset               Reset to default color and pattern.
  --pattern {sine,solid,siren,strobe,fadein,fadeout}
                        Set LED flash pattern.
  --color red green blue
                        Set LED red, green, and blue brightness values. (range
                        0 - 255)
  --applyto {all,front_left,front_right,back_left,back_right}
                        Apply settings to LED(s)
  --ip protocol:ipAddress:port
                        Protocol / IP address / Port number for connection
~~~~~

To use the script, you first specify settings or actions with "--color", "--pattern", or "--reset", followed by the LED's to which the settings should be applied using the "--applyto" option.

## Reset
The "--reset" option is used to reset the LED's to their default system colors (typically red and white).

For example, to reset all of the LED's, execute the following command.

`led_control.py --reset --applyto all`

## Color
The "--color" option sets the color of the LED(s) using the supplied brightness values for red, green, and blue. The brightness can range from 0 (off) to 255 (full brightness). "--color" can also be combined with "--pattern" to specify the illumination pattern. (see Pattern below)

Some examples:

Set front_left LED to blue:

`led_control.py --color 0 0 255 --applyto front_left`

Set all LED's to yellow:

`led_control.py --color 255 255 0 --applyto all`

Set the back (rear) LED's to orange:

`led_control.py --color 255 64 0 --applyto back_left --applyto back_right`

## Pattern
The "--pattern" option is used to specify the illumination pattern for the LED's. "--pattern" can be used with or without a color. If "--pattern" is specified without "--color", the color defaults to white.

For example, to set all LED's to yellow, with a "strobe" pattern:

`led_control.py --color 255 255 0 --pattern strobe --applyto all`

## Combining options 

Finally, you can combine different settings for different LED's into a single command:
`led_control.py --reset all --color 255 128 32 --applyto front_left --applyto front_right --color 0 0 255 --flash strobe --applyto back_left --applyto back_right`

The "--applyto" option will take the preceding settings and apply them to the given LED.

