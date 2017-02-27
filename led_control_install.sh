#!/bin/sh -e
INSTALL_SCRIPT_VERSION=0.01
ZIP_FILE=led_control_files.zip

echo "*** Installing Solo LED Control ***"

tempdir=$(mktemp -d)
echo "Created temporary directory ${tempdir}"

echo "Unpacking solo_led_files.zip into ${tempdir}"
unzip -q ${ZIP_FILE} -d ${tempdir}

if [ ! -f ${tempdir}/version_${INSTALL_SCRIPT_VERSION} ]
then
  echo "Error: install script version does not match version of ${ZIP_FILE}"
  exit
fi

echo "Making /usr/local/bin directory"
mkdir -p /usr/local/bin

echo "Copying files to Solo filesystem"
cp -v ${tempdir}/led_control.py /usr/local/bin
cp -v ${tempdir}/SoloLED.py /usr/local/bin
cp -v ${tempdir}/init_leds.sh /etc/init.d

if [ ! -a /etc/default/init_leds ]
then
  cp ${tempdir}/init_leds /etc/default
fi

echo "Setting permissions"
chmod 744 /usr/local/bin/led_control.py
chmod 744 /etc/init.d/init_leds.sh

echo "Activating boot script"
update-rc.d init_leds.sh start 90 4 .

echo "Preparing firmware upgrade"
cp -v ${tempdir}/ArduCopter-v2.px4 /firmware

echo "Cleaning up"
rm -r ${tempdir}
rm  ${ZIP_FILE}
rm "$0"

echo "Sync filesystem"
sync

echo "Rebooting"
reboot


