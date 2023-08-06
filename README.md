# BeepBerry Sensors Carrier

Integrates UBlox GPS, IMU/MAG, BARO, and buzzer.

** WARNING!!! --- THIS IS AN UNVERIFIED DESIGN!!! --- WARNING!!! **

![media/populated_board.png](media/populated_board.png)

![media/board_installed.gif](media/board_installed.gif)

![media/close_up.gif](media/close_up.gif)

![media/sensor_addon.gif](media/sensor_addon.gif)

## Using the buzzer

### Simple Tones
```
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
```

### ALSA

In `/boot/config.txt`, add:

```
dtoverlay=audremap,enable_jack=on
dtoverlay=pwm-2chan,pin2=13,func2=4
```

then use anything that uses a sound card, IE:

`espeak "SAY SOMETHING"`

`aplay "some.wav"`
