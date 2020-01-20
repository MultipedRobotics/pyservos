#!/usr/bin/env python

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
# ----------------------------
# Simple tool to work with AX-12 servos
#

from ax12 import AX12
from pyservos.servoserial import ServoSerial
import sys
import argparse
import time
from pingbin import ping
from setidbin import set_id
from setanglebin import set_angle

# def handleArgs():
#     parser = argparse.ArgumentParser(description='set servo id')
#     parser.add_argument('-i', '--interactive', help='input via commandline', action='store_true')
#     parser.add_argument('-n', '--new_id', help='set new id', type=int, default=1)
#     parser.add_argument('-c', '--current_id', help='current id', type=int, default=1)
#     parser.add_argument('port', help='serial port', type=str)
#
#     args = vars(parser.parse_args())
#     return args

# args = handleArgs()

port = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A904MISU-if00-port0"
ser = ServoSerial(port)
try:
    ser.open()
except Exception as e:
    print('-'*40)
    print(sys.argv[0], ':')
    print(e)
    exit(1)

# ping()
# set_id(1, 2, ser)
# ping(ser)
set_angle(2, 150+45, ser)
time.sleep(1)
set_angle(2, 150, ser)
time.sleep(1)
set_angle(2, 150-45, ser)
time.sleep(1)
set_angle(2, 150, ser)
time.sleep(1)


set_angle(1, 150, ser)
time.sleep(1)
set_angle(1, 150+20, ser)
time.sleep(1)
set_angle(1, 150, ser)
time.sleep(1)
set_angle(1, 150-20, ser)
time.sleep(1)
set_angle(1, 150, ser)
time.sleep(1)

ser.close()
