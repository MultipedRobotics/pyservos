#!/usr/bin/env python

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
# ----------------------------
# Simple tool to change the id number of a servo
#

from __future__ import print_function, division
from pyservos import Packet
from pyservos import ServoSerial
import pyservos
import argparse


def handleArgs():
	parser = argparse.ArgumentParser(description='Resets servo(s) to factory defaults')
	parser.add_argument('-a', '--all', help='reset all servos to defaults', action='store_true')
	parser.add_argument('-i', '--id', help='servo id', type=int, default=1)
	parser.add_argument('port', help='serial port or \'dummy\' for testing', type=str)

	args = vars(parser.parse_args())
	return args


def main():
	args = handleArgs()

	port = args['port']

	servo = Packet(pyservos.AX12)

	if args['all']:
		ID = servo.base.BROADCAST_ADDR
	else:
		ID = args['id']

	ser = ServoSerial(port=port)
	ser.open()

	pkt = servo.makeRebootPacket(ID)

	ser.write(pkt)
	gramar = 'is'
	if ID == servo.base.BROADCAST_ADDR:
		ID = 'all'
		gramar = 'are'
	print('Servo[{}] {} rebooting'.format(ID, gramar))


if __name__ == '__main__':
	main()
