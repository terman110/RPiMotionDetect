#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home
cd /
cd /home/pi/projects/RPiMotionDetect
sudo python motion.py >> log/log.txt 2>&1 &
cd /
