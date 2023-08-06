#!/usr/bin/python3
##################

import smbus
import time
from bmp388 import BMP388_I2C
from bmx160 import BMX160
import gps

gpsd = gps.gps(mode=gps.WATCH_ENABLE)

i2c_1 = smbus.SMBus(1)
bmp388 = BMP388_I2C(i2c_1)

bmx160 = BMX160(1)
bmx160.begin()

# clear screen
print('\033[2J')

while True:

  # read gps before clearing the screen, since it blocks
  gpsd.read()

  # clear the screen
  print('\033[2J')

  # goto cursor 0,0
  print('\033[0;0H')

  # print gps
  #if (gps.MODE_SET & gpsd.valid):

  print('Mode: %s(%d)\n' %
       (('Invalid', 'NO_FIX', '2D', '3D')[gpsd.fix.mode],
       gpsd.fix.mode), end='')

  #if gps.TIME_SET & gpsd.valid:
  print('Time: ' + str(gpsd.fix.time))
  #else:
  #  print('Time: ---')

  if ((gps.isfinite(gpsd.fix.latitude) and
    gps.isfinite(gpsd.fix.longitude))):
    print('Lat %.8f' % (gpsd.fix.latitude))
    print('Lon %.8f' % (gpsd.fix.longitude))
  else:
    print('Lat: ---')
    print('Lon: ---')

  # print baro
  print('')
  print('Altitude (m): ' + '{:10.3f}'.format(bmp388.readAltitude()))
  print('Pressure (hPa): ' + '{:10.3f}'.format(bmp388.readPressure()/100.0))
  print('Temperature (C): ' + '{:10.3f}'.format(bmp388.readTemperature()))

  # print imu
  print('')
  data = bmx160.get_all_data()
  print('ACC: ' + '{:10.3f}'.format(data[6]) + '{:10.3f}'.format(data[7]) + '{:10.3f}'.format(data[8]))
  print('GYR: ' + '{:10.3f}'.format(data[3]) + '{:10.3f}'.format(data[4]) + '{:10.3f}'.format(data[5]))
  print('MAG: ' + '{:10.3f}'.format(data[0]) + '{:10.3f}'.format(data[1]) + '{:10.3f}'.format(data[2]))

  time.sleep(0.1)

