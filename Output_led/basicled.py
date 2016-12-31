#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

#Disable warnings
GPIO.setwarnings(False)

#Set the mode to breakout board with bredboard Broadcom
GPIO.setmode(GPIO.BCM)

#Set up a channel, in this case enable the pin number 4 as output
GPIO.setup(4, GPIO.OUT)

#Just loop each to seconds between on and off
while True:
    GPIO.output(4, True)
    time.sleep(2)
    GPIO.output(4,False )
    time.sleep(2)



