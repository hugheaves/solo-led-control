#! /bin/sh
### BEGIN INIT INFO
# Provides:          led_control
# Required-Start:
# Required-Stop:
# Default-Start:     4
# Default-Stop:
# Short-Description: Set LED colors at startup
### END INIT INFO

PATH=/sbin:/usr/sbin:/bin:/usr/bin

LED_SETTINGS="--reset --applyto all"

if test -f /etc/default/init_leds; then
    . /etc/default/init_leds
fi

do_start() {
	sh -c "
	sleep 20;
	/bin/date > /var/log/init_leds.log;
	/home/root/led_control.py --reset --applyto all >> /var/log/init_leds.log 2>&1;
	/home/root/led_control.py ${LED_SETTINGS}  >> /var/log/init_leds.log 2>&1;
	" &
}

case "$1" in
    start)
	do_start
        ;;
    restart|reload|force-reload)
        echo "Error: argument '$1' not supported" >&2
        exit 3
        ;;
    stop)
        ;;
    *)
        echo "Usage: $0 start|stop" >&2
        exit 3
        ;;
esac
