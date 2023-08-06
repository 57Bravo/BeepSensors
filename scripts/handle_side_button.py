#!/usr/bin/python3
##################

import RPi.GPIO as GPIO
import time
import os

# const's

## button
GPIO_SIDE_BUTTON = 17
BUTTON_PRESSED = 0
BUTTON_RELEASED = True
POLL_TIMEOUT_SECS = 0.1

## display
SCREEN_ON = True
SCREEN_DEV = '/sys/class/graphics/fb1'
KEYBOARD_DEV = '/sys/class/input/input0'
TOUCHPAD_DEV = '/sys/class/input/input1'
CONSOLE_DEV = '/dev/tty1'
SILENCE = ' > /dev/null 2>&1'

## commands, relies on sysfs and escap sequences

### blank the screen
SCREEN_OFF_CMD_1 = 'bash -c "echo 1 > ' + SCREEN_DEV + '/blank"' + SILENCE
### disable
SCREEN_OFF_CMD_2 = 'echo 1 > ' + SCREEN_DEV + '/state'

### disable keyboard
KEYBOARD_DISABLE = 'echo 1 > ' + KEYBOARD_DEV + '/inhibited'
### disable touchpad
TOUCHPAD_DISABLE = 'echo 1 > ' + TOUCHPAD_DEV + '/inhibited'

### show the screen
SCREEN_ON_CMD_1 = 'bash -c "echo 0 > ' + SCREEN_DEV + '/blank"' + SILENCE
### enable
SCREEN_ON_CMD_2 = 'echo 0 > ' + SCREEN_DEV + '/state'

### enable keyboard
KEYBOARD_ENABLE = 'echo 0 > ' + KEYBOARD_DEV + '/inhibited'
### enable touchpad
TOUCHPAD_ENABLE = 'echo 0 > ' + TOUCHPAD_DEV + '/inhibited'

# setup the side button with a pull-up
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_SIDE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# poll the button
while True:

  # wait for a button press
  if GPIO.input(GPIO_SIDE_BUTTON) == BUTTON_PRESSED:

    # track the release
    if BUTTON_RELEASED:
      BUTTON_RELEASED = False

      # ON to OFF
      if SCREEN_ON:
        SCREEN_ON = False
        os.system(SCREEN_OFF_CMD_1)
        os.system(SCREEN_OFF_CMD_2)
        os.system(KEYBOARD_DISABLE)
        os.system(TOUCHPAD_DISABLE)
      # OFF to ON
      else:
        SCREEN_ON = True
        os.system(SCREEN_ON_CMD_1)
        os.system(SCREEN_ON_CMD_2)
        os.system(KEYBOARD_ENABLE)
        os.system(TOUCHPAD_ENABLE)

  else:
    BUTTON_RELEASED = True

  # don't thrash
  time.sleep(POLL_TIMEOUT_SECS)
