RPiMotionDetect
===========

##Introduction

A python script for the Raspberry PI B (and newer) dat controls a relay depending on motion. It uses a HC-SR501 PIR motion detector (pin 24, GND to GND on pi, 5v to 5V on pi) and a one port 5V relay (pin 23, GND to GND on pi, 5V to 3.3V on pi) module.

![GPIOs](/img/gpio.png?raw=true "GPIOs")
![PIR](/img/pir.jog?raw=true "PIR")

##Auto run on pi

We need to make the launcher script an executable, which we do with this command

	chmod 775 launcher.sh

Now test it

	sh launcher.sh

Add to crontab

	sudo crontab -e

Add line

	@reboot sh /home/pi/projects/RPiMotionDetect/launcher.sh >/home/pi/projects/RPiMotionDetect/log/log.txt 2>&1
