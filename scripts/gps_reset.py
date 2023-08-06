#!/usr/bin/python3
##################

import RPi.GPIO as GPIO
import time
import os

GPS_RESET_GPIO = 18
GPIO.setmode(GPIO.BCM)

GPIO.setup(GPS_RESET_GPIO, GPIO.OUT)

GPIO.output(GPS_RESET_GPIO, 0)
time.sleep(5)
GPIO.output(GPS_RESET_GPIO, 1)

