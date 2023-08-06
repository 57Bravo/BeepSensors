#!/usr/bin/python3
##################

import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

pwm = GPIO.PWM(13, 57)
pwm.start(10)

for i in range(random.randint(0,10)):
  pwm.ChangeFrequency(random.randint(1,10000))
  time.sleep(random.random())
pwm.stop()
