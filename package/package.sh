#!/bin/sh -x

zipfile=$(mktemp).zip
rm $zipfile
currentDir=$(pwd)
cd ../files
zip -r ${zipfile} .
cd ${currentDir}
cat ./install_led_control_base.sh ${zipfile} > ../install_led_control.sh
