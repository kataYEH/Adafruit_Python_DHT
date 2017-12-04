#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	Switch = GPIO.input(24)
	if (Switch == 0):
		print("button pressed!")
	else:
		print("OFF")
	time.sleep(1)

