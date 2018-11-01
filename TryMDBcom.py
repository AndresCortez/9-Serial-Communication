#!/usr/bin/env python

# bb_serial.py
# 2014-12-23
# Public Domain

# bit bang transmit and receive of serial data
#
# tested by connecting the arbitrary RX/TX gpios to a USB
# serial dongle plugged in to a Linux box.
#
# on the Linux box set the baud and data bits (cs5-cs8)
#
# stty -F /dev/ttyUSB0 19200 cs8
# cat </dev/ttyUSB0 >/dev/ttyUSB0
#
# so the Linux box echoes back data received from the Pi.
#
# laptop timings deviations
#
# baud  exp us   act us
#   50   20000    13310 * 75
#   75   13333    13310
#  110    9091    13310 * 75
#  134    7462     6792 * 150
#  150    6667     6792
#  200    5000     6792 * 150
#  300    3333     3362
#

import sys
import time
import difflib

import pigpio

RX=15
TX=14

pi = pigpio.pi()
pi.set_mode(TX, pigpio.OUTPUT)
pi.set_mode(RX, pigpio.INPUT)
# fatal exceptions off (so that closing an unopened gpio doesn't error)

pigpio.exceptions = False

pi.bb_serial_read_close(RX)

# fatal exceptions on

pigpio.exceptions = True

# create a waveform representing the serial data

pi.wave_clear()
pi.wave_add_serial(TX,9600,'A',0,8,2)
wid=pi.wave_create()
# open a gpio to bit bang read the echoed data
pi.bb_serial_read_open(RX, 9600,9)
count = 1
print("Data Serial Read and Write")
while 1:
  #while count > 0:
  (count,data) = pi.bb_serial_read(RX)
  if count > 0:
    print data
    #for x in range(count):
      #print data[x] 
  time.sleep(2) # enough time to ensure more data
      
  pi.wave_send_once(wid)   # transmit serial data
  while pi.wave_tx_busy(): # wait until all data sent
    pass

# free resources

pi.wave_delete(wid)

pi.bb_serial_read_close(RX)

pi.stop()