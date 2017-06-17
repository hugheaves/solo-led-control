#!/bin/sh -e
INSTALL_SCRIPT_VERSION=0.09

echo "*** Installing Solo LED Control Version ${INSTALL_SCRIPT_VERSION} ***"

tempfile=$(mktemp)
zipfile=${tempfile}.zip
mv ${tempfile} ${zipfile}

echo "Extracting zip file data from ${0} into ${zipfile}"

# Binary payload idea from http://www.linuxjournal.com/content/add-binary-payload-your-shell-scripts
match=$(grep -aon '^PAYLOAD:$' $0 | cut -d ':' -f 1)
if [ ${match} != "" ]; then
    payload_start=$((match + 1))
    tail -n +$payload_start $0 > ${zipfile}
else
    echo "Error finding zip file data"
    exit
fi

tempdir=$(mktemp -d)
echo "Created temporary directory ${tempdir}"

echo "Unpacking ${zipfile} into ${tempdir}"
unzip -q ${zipfile} -d ${tempdir}

if [ ! -f ${tempdir}/version_${INSTALL_SCRIPT_VERSION} ]
then
  echo "Error: install script version does not match zip file version"
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
else
  cp ${tempdir}/init_leds /etc/default/init_leds.NEW
fi

echo "Making .ssh directory"
mkdir /home/root/.ssh

echo "Copying SSH environment settings"
if [ ! -a /home/root/.ssh/environment ]
then
  cp ${tempdir}/environment /home/root/.ssh/
fi

echo "Updating sshd configuration"
sed -ie 's/^#UseDNS yes$/UseDNS no/g' /etc/ssh/sshd_config
sed -ie 's/^#PermitUserEnvironment no$/PermitUserEnvironment yes/g' /etc/ssh/sshd_config

echo "Setting permissions"
chmod 744 /usr/local/bin/led_control.py
chmod 744 /etc/init.d/init_leds.sh

echo "Removing old files"
rm -f /home/root/led_control.py
rm -f /home/root/SoloLED.py

echo "Activating boot script"
update-rc.d init_leds.sh start 90 4 .

if [ $1 == "install_firmware" ]
then
	echo "Preparing firmware upgrade"
	cp -v ${tempdir}/ArduCopter-v2.px4 /firmware
else
	echo "Skipping firmware upgrade"
fi

echo "Cleaning up"
rm -r ${tempdir}
rm  ${zipfile}
rm "$0"

echo "Sync filesystem"
sync

echo "Rebooting"
reboot

exit

PAYLOAD:
