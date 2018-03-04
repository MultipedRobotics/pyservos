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
from pyservos.utils import angle2int, le
import argparse


DESCRIPTION = """
Set the angle of a servo in degrees.

Example: set servo 3 to angle 45

./set_angle /dev/serial0 45 -i 3
"""


def handleArgs():
	parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-i', '--id', help='servo id', type=int, default=0)
	parser.add_argument('port', help='serial port  or \'dummy\' for testing', type=str)
	parser.add_argument('angle', help='servo angle in degrees: 0.0 - 300.0', type=float)
	parser.add_argument('-s', '--speed', help='servo speed: 1 - 1023', type=int, default=0)

	args = vars(parser.parse_args())
	return args


def main():
	args = handleArgs()

	ID = args['id']
	port = args['port']
	angle = args['angle']
	speed = args['speed']

	print('Setting servo[{}] to {:.2f} on port {}'.format(ID, angle, port))

	serial = ServoSerial(port=port)
	serial.open()

	servo = Packet(pyservos.AX12)

	# pkt = servo.makeServoMovePacket(ID, angle)
	val = angle2int(angle, degrees=True) + le(speed)
	pkt = servo.makeWritePacket(ID, servo.base.GOAL_POSITION, val)
	ans = serial.sendPkt(pkt)  # send packet to servo
	if ans:
		print('status: {}'.format(ans))


if __name__ == '__main__':
	main()
