#!/usr/bin/env python

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################

from __future__ import print_function
from pyservos import Packet
from pyservos.servoserial import ServoSerial
import pyservos
from pyservos.utils import angle2int, le
import time

ID = 1

port = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A904MISU-if00-port0"
serial = ServoSerial(port=port)
serial.open()

servo = Packet(pyservos.AX12)

# pkt = servo.makeServoMovePacket(ID, angle)
# val = angle2int(angle, degrees=True) + le(speed)
pkt = servo.makeWritePacket(ID, servo.base.CW_ANGLE_LIMIT, [0,0])
ans = serial.sendPkt(pkt)  # send packet to servo

pkt = servo.makeWritePacket(ID, servo.base.CCW_ANGLE_LIMIT, [0,0])
ans = serial.sendPkt(pkt)  # send packet to servo


speed = 2000
pkt = servo.makeWritePacket(ID, servo.base.GOAL_VELOCITY, le(speed))
ans = serial.sendPkt(pkt)  # send packet to servo

time.sleep(3)


speed = 0
pkt = servo.makeWritePacket(ID, servo.base.GOAL_VELOCITY, le(speed))
ans = serial.sendPkt(pkt)  # send packet to servo
