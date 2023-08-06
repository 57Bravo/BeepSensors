#!/usr/bin/python3
##################

import sys
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

gps_out = open(sys.argv[1], 'w')
gps_out.write('fix,time,lat,lon,gps_alt,baro_alt,press,temp,acc_x,acc_y,acc_z,gyr_x,gyr_y,gyr_z,mag_x,mag_y,mag_z\n')

while True:

  # read gps before clearing the screen, since it blocks
  gpsd.read()

  gps_out.write('%s' % ('Invalid', 'NO_FIX', '2D', '3D')[gpsd.fix.mode])
  gps_out.write(',' + str(gpsd.fix.time))
  gps_out.write(',%.8f' % (gpsd.fix.latitude))
  gps_out.write(',%.8f' % (gpsd.fix.longitude))
  gps_out.write(',%.8f' % (gpsd.fix.altitude))
  gps_out.write(',' + '{:0.3f}'.format(bmp388.readAltitude()))
  gps_out.write(',' + '{:0.3f}'.format(bmp388.readPressure()/100.0))
  gps_out.write(',' + '{:0.3f}'.format(bmp388.readTemperature()))
  data = bmx160.get_all_data()
  gps_out.write(',' + '{:0.3f}'.format(data[6]) + ',{:0.3f}'.format(data[7]) + ',{:0.3f}'.format(data[8]))
  gps_out.write(',' + '{:0.3f}'.format(data[3]) + ',{:0.3f}'.format(data[4]) + ',{:0.3f}'.format(data[5]))
  gps_out.write(',' + '{:0.3f}'.format(data[0]) + ',{:0.3f}'.format(data[1]) + ',{:0.3f}\n'.format(data[2]))

  time.sleep(0.1)

