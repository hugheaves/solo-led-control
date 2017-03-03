# Disclaimer
Gaining full control of the LED's on your 3DR Solo requires installing non-factory / unsupported software on your 3DR Solo. **Doing so will almost certainly void your warranty, and could cause irreparable damage to your Solo or other property, personal injury, or even loss of life. Proceed with caution**.

Therefore, from the GPL, under which this software is licensed:

> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# Installation
**Warning: This process will install a non-standard version of 3DR Solo ArduCopter v1.5.3 firmware on your solo.**

These instructions are written for users already somewhat familiar with SSH, file transfer, executing scripts, etc.

1. Download the following files:
[install_led_control.sh](https://raw.githubusercontent.com/hugheaves/solo-led-control/v0.0.3/install_led_control.sh)

2. Using an SSH file transfer client such as [WinSCP](https://winscp.net/), copy the downloaded files to your 3DR Solo. (The IP address of Solo is 10.1.1.10, and the root password is "TjSDBkAu".)

3. Using either Solex, or an SSH terminal client such as [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/) execute the following command:

`sh ./install_led_control.sh`

If everything is working, you should see the following output, and your Solo will reboot. You will see "rainbow colored LED's" while the new firmware is installed. Then your Solo will show the normal "red/white" LED pattern, and after 20-30 more seconds, the pattern will change to standard aviation colors.

~~~~~
*** Installing Solo LED Control ***
Created temporary directory /tmp/tmp.EYfone
Unpacking solo_led_files.zip into /tmp/tmp.EYfone
Making /usr/local/bin directory
Copying files to Solo filesystem
Setting permissions
Activating boot script
 System startup links for /etc/init.d/init_leds.sh already exist.
Preparing firmware upgrade
Cleaning up
Sync filesystem
Rebooting
~~~~~


# Usage
Once everything is installed, you can use the `led_control.py` script to control Solo's LEDs. You can run the script using Solex's "command" feature, or via an interactive SSH connection.

The command to run the script is:

`led_control.py`

Running the script with the "-h" option will display help information:

`led_control.py -h`

~~~~~
usage: led_control.py [-h]
                      [--reset {all,front_left,front_right,back_left,back_right}]
                      [--pattern {sine,solid,siren,strobe,fadein,fadeout}]
                      [--phaseOffset degrees] [--period period]
                      [--repeat count] [--color red green blue]
                      [--amplitude red green blue]
                      [--applyto {all,front_left,front_right,back_left,back_right}]
                      [--ip protocol:ipAddress:port]

optional arguments:
  -h, --help            show this help message and exit
  --reset {all,front_left,front_right,back_left,back_right}
                        Reset to default color and pattern.
  --pattern {sine,solid,siren,strobe,fadein,fadeout}
                        Set LED flash pattern.
  --phaseOffset degrees
                        Set phase offset in degrees (range 0-360).
  --period period       Set period in milliseconds (range 0-4000).
  --repeat count        Set repeat count (0-255).
  --color red green blue
                        Set LED red, green, and blue brightness values. (range
                        0 - 255)
  --amplitude red green blue
                        Set LED red, green, and blue amplitude values. (range
                        0 - 255)
  --applyto {all,front_left,front_right,back_left,back_right}
                        Apply settings to LED(s)
  --ip protocol:ipAddress:port
                        Protocol / IP address / Port number for connction
~~~~~

## Basic Information
The `led_control.py script provideds command line options to set LED colors and patterns, and these settings can be applied to individual LED's, or all LED's at once.

## Resetting LED's
The "--reset" option is used to reset the LED's to their default system colors (typically red and white). To reset LED's, use the "--reset" command line option, followed by the LED that you would like to reset. (either individual or "all").

For example, to reset all of the LED's, execute the following command.

`led_control.py --reset all`

You can reset individual LED's like this:

`led_control.py --reset front_left`

You can issue multiple reset commands at once like this:

`led_control.py --reset front_left --reset front_right`

## Setting Colors, Patterns, etc.
Individual command line options are provided to change the various LED settings (color, pattern, etc.). To change some settings, you first specify the settings you would like to change, and then use the `--applyto` option to specify which LEDs you'd like to change. For example, to set all of the LED's to strobing green, the command would be:

`led_control.py --pattern strobe --color 0 255 0 --applyto all`

The `--applyto` options applies any settings appearing before it (not after it) on the command line. Any settings that have not been specified take on the default values listen in each section below.

### Color

**Default value:** 255 255 255 (white)
**Range:** 0 - 255 for each value

The "--color" option sets the color of the LED(s) using the supplied brightness values for red, green, and blue. The brightness can range from 0 (off) to 255 (full brightness). "--color" can also be combined with "--pattern" to specify the illumination pattern. (see Pattern below)

Some examples:

Set front_left LED to blue:

`led_control.py --color 0 0 255 --applyto front_left`

Set all LED's to yellow:

`led_control.py --color 255 255 0 --applyto all`

Set the back (rear) LED's to orange:

`led_control.py --color 255 64 0 --applyto back_left --applyto back_right`

### Pattern

**Default value:** solid

The "--pattern" option is used to specify the illumination pattern for the LED's. "--pattern" can be used with or without a color. If "--pattern" is specified without "--color", the color defaults to white.

For example, to set all LED's to yellow, with a "strobe" pattern:

`led_control.py --color 255 255 0 --pattern strobe --applyto all`

## Note: Due to what appears to be a bug in the OreoLED firmware, the following two options (phase offset, period) only work with the "strobe" pattern.

### Phase Offset

**Default value:** 0 degrees
**Range:** 0 - 360 degrees

The Solo LED patterns are repeating waves with a 360 degree cycle length. You can specify phase offsets for the pattern to have different LED's be in different parts of the pattern at the same time. 

For example, by setting a 180 degree phase offset, you can have the front and back LEDs have an alternating blink:

`led_control.py --phase_offset 0 --applyto front_left --applyto front_right`
`led_control.py --phase_offset 180 --applyto back_left --applyto back_right`

### Period

**Default value:** 2000 milliseconds
**Range:** 0 - 4000 milliseconds

Period specifies the the repeat period (interval) for the pattern, from 0 - 4 seconds (4000 milliseconds). 

For example, to set a fast blinking pattern on all LED's:

`led_control.py --pattern strobe --period 300 --applyto all`

### Amplitude

**Default value:** 0 0 0 
**Range:** 0 - 255 for each value

**This option currently does not work.**

## Multiple `--applyto` options

`--applyto` can appear multiple times, to apply different settings to different LEDs. Apply to still applies all settings that appear before it on the command line, even those prior to another applyto. This is actually useful to set some "base settings", and then apply more specific settings to each LED.

For example, to set the front LEDs to solid red, and the back LED's to strobing red, the `--color` option only has to be specified once:

`led_control.py --color 255 0 0 --applyto front_left --applyto front_right --pattern strobe --applyto back_left --applyto back_right`

# Reducing Delay When Running Commands with Solex
Solex uses an SSH connection to Solo to run commands. Unfortunately, Solo's SSH server is configured in a way that makes is slow to respond to SSH connection requests. There is a quick fix that you can make to greatly decrease the amount of time it takes Solo to respond.

To fix the problem, open an SSH terminal connection to Solo (10.1.1.10), and execute the following command

`echo "UseDNS no" >> /etc/ssh/sshd_config`

You can also just edit the file, and add a line at the bottom with `UseDNS no`.

Either way, you only need to do this once, as the change will persist between reboots.

## IP Address
By default, the script connects to the same system on which it is run. So, when it's run on Solo, it connects to Solo. You can also run the script on other systems that have the mavlink libraries installed. If you do that, you'll need to specify a different ip address (connect string) when you run the script. Normally, you would use "udpin:0.0.0.0:14550", like this:

`led_control.py --ip udpin:0.0.0.0:14550`

# Customizing startup color settings

The startup colors are set in the `/etc/default/init_leds` file on your Solo. Edit this file with whatever led_control options you would like to be used at system startup.

# Disabling startup color settings

Deleting the `/etc/default/init_leds` file on your Solo will prevent the colors being set on startup.

# Acknowledgements

Thanks to Pedals2Paddles @ 3DRForums for the positive feedback, suggestions, the "aviation standard lighting", and the patience to work through my crappy instructions. :)




