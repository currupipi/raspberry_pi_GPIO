#!/usr/bin/env python
# This script requires that you install mpg123 on the raspberrypi as it will be executed 
# by subprocess
# Also you need the ok.mp3 and fail.mp3 audio tracks, to live in the same directory
# you have the script, feel free to download them from any legal source of mp3 downloads.
# The ones in that repo are from freesound.org

import subprocess
import sys
import RPi.GPIO as GPIO

#Disable warnings
GPIO.setwarnings(False)

#Set the mode to breakout board with bredboard Broadcom
GPIO.setmode(GPIO.BCM)

#Set up a channel, in this case enable the pin number 4 as button input
GPIO.setup(4, GPIO.IN)

print "Hey press the BUTOOONNNN hurry up!!!!!"

#Wait for the button to play some nice music before timeout expires
press = GPIO.wait_for_edge(4, GPIO.FALLING, timeout=5000)

if press is None:
    print "You are too slow.. shame on you"
    command = 'mpg123 fail.mp3 2> /dev/null'
    try:
        subprocess.call(command, shell=True)
	print "Press the button faster"
    except:
	print "Can not play the fail music :-("
        sys.exit(2)
else:
    print "That's the way I like it"
    command = 'mpg123 ok.mp3 2> /dev/null'
    try:
        subprocess.call(command, shell=True)
	print "Well done!"
    except:
	print "Can not play the hurray music :-("
        sys.exit(3)

#Clean all once done
GPIO.cleanup()
