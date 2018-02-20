#!/usr/bin/env python

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################

from __future__ import print_function
from pyservos import Packet
from pyservos import ServoSerial
import pyservos


port = "/dev/tty.usbserial-AL034G1T"
ID = 1
angle = 200

serial = ServoSerial(port=port)
serial.open()

servo = Packet(pyservos.AX12)
# servo = Packet(pyservos.XL320)

pkt = servo.makeServoMovePacket(ID, angle)
ans = serial.sendPkt(pkt)  # send packet to servo
ans = servo.processStatusPacket(ans)

if ans:
	print('status: {}'.format(ans))
