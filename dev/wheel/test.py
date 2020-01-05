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

def set_wheel_mode(ID):
    """
    This will over write CW_ANGLE_LIMIT and CCW_ANGLE_LIMIT
    """
    pkt = servo.makeWritePacket(ID, servo.base.CW_ANGLE_LIMIT, [0,0,0,0])
    return pkt

def set_joint_mode(ID):
    """
    This will over write CW_ANGLE_LIMIT and CCW_ANGLE_LIMIT
    """
    pkt = servo.makeWritePacket(ID, servo.base.CW_ANGLE_LIMIT, [0,0] + le(1023))
    return pkt

def set_wheel_speed(ID, speed):
    """
    Sets speed of wheel, all values are integers:
        positive [0 to 1023]: CW
        negative [-1023 to 0]: CCW

    For the servo, the values are:
        0, 1024:   Stop
        1-1023:    CW
        1025-2047: CCW

    Bit 10 determines direction, 0:CW, 1:CCW
    """
    speed = 1023 if speed > 1023 else speed
    if speed < 0:
        speed = -1023 if speed < -1023 else speed
        speed = 1024 + abs(speed)

    pkt = servo.makeWritePacket(ID, servo.base.GOAL_VELOCITY, le(speed))
    return pkt


ID = 1

port = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A904MISU-if00-port0"
# port = "/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0"
serial = ServoSerial(port=port)
serial.open()

print(">> baudrate:", serial.serial.baudrate)

servo = Packet(pyservos.AX12)

pkt = set_wheel_mode(ID)
ans = serial.sendPkt(pkt)  # send packet to servo

for speed in range(-1023, 1023, 10):
    print(">>", speed)
    pkt = set_wheel_speed(ID, speed)
    ans = serial.sendPkt(pkt)  # send packet to servo
    time.sleep(0.1)


speed = 0
# pkt = servo.makeWritePacket(ID, servo.base.GOAL_VELOCITY, le(speed))
pkt = set_wheel_speed(ID, speed)
ans = serial.sendPkt(pkt)  # send packet to servo
