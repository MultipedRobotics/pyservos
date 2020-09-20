#!/usr/bin/env python3

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################

# from __future__ import print_function
# from pyservos import Packet
# from pyservos import ServoSerial
import pyservos
import sys
from pyservos.ax12 import AX12
from pyservos.servo_serial import ServoSerial


# you will need to CHANGE this to the correct port
# port = "/dev/tty.usbserial-A506BOT5"
port = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A904MISU-if00-port0"
ID = 1
# angle = int(sys.argv[1])

# print('Setting servo[{}] to {:.2f} on port {}'.format(ID, angle, port))

try:
	serial = ServoSerial(port=port)
	serial.open()
except Exception as e:
	print(e)
	print('Oops, wrong port')
	print('bye ....')
	exit(1)

# if True:
servo = AX12()
print('We are talking to an AX12 servo')
# else:
# 	servo = Packet(pyservos.XL320)
# 	print('We are talking to an XL320 servo')

pkt = servo.makeReadPacket(ID, 30, [2])
ans = serial.sendPkt(pkt)  # send packet to servo
ans = servo.processStatusPacket(ans)

if ans:
	print('status: {}'.format(ans))
