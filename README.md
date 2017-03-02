# Disclaimer
Gaining full control of the LED's on your 3DR Solo requires installing non-factory / unsupported software on your 3DR Solo. **Doing so will almost certainly void your warranty, and could cause irreparable damage to your Solo or other property, personal injury, or even loss of life. Proceed with caution**.

Therefore, from the GPL, under which this software is licensed:

> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# Installation
**Warning: This process will install a non-standard version of 3DR Solo ArduCopter v1.5.3 firmware on your solo.**

These instructions are written for users already familar with SSH, file transfer, executing scripts, etc.

1. Download the following files:
[install_led_control.sh](https://raw.githubusercontent.com/hugheaves/solo-led-control/v0.0.1/install_led_control.sh)

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
Once everything is installed, you can run the `led_control.py` script to control the LEDs on Solo. You can run the script using Solex's "command" feature, or via an interactive SSH connection.

The command to run the script is:

`led_control.py`

Running the script with the "-h" option will display help on the options available in the script:

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

To use the script, you first specify settings or actions with "--color", "--pattern", or "--reset", followed by "--applyto", specifying to which LED's the settings should be applied.

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

`led_control.py --reset --applyto all --color 255 128 32 --applyto front_left --applyto front_right --color 0 0 255 --pattern strobe --applyto back_left --applyto back_right`


# Reducing Delay When Running Commands with Solex
Solex uses an SSH connection to Solo to run commands. Unfortunately, Solo's SSH server is configured in a way that makes is slow to respond to SSH connection requests. There is a quick fix that you can make to greatly decrease the amount of time it takes Solo to respond.

To fix the problem, open an SSH terminal connection to Solo (10.1.1.10), and execute the following command

`echo "UseDNS no" >> /etc/ssh/sshd_config`

You can also just edit the file, and add a line at the bottom with `UseDNS no`.

Either way, you only need to do this once, as the change will persist between reboots.

# Customizing startup color settings

The startup colors are set in the `/etc/default/init_leds` file on your Solo. Edit this file with whatever led_control options you would like to be used at system startup.

# Disabling startup color settings

Deleting the `/etc/default/init_leds` file on your Solo will prevent the colors being set on startup.

# Acknowledgements

Thanks to Pedals2Paddles @ 3DRForums for the positive feedback, suggestions, the "standard aeronautical lighting settings", and the patience to work through my crappy instructions. :)




