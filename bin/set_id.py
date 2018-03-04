#!/usr/bin/env python

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
# ----------------------------
# Simple tool to change the id number of a servo
#

from __future__ import print_function
from pyservos import Packet
from pyservos import ServoSerial
import sys
import argparse
import time
import pyservos
PY3 = sys.version_info > (3,)


def get_input(s):
	"""Handle difference between py2 and py3"""
	if PY3:
		return input(s)
	else:
		return raw_input(s)


# def makeServoIDPacket(curr_id, new_id):
# 	"""
# 	Given the current ID, returns a packet to set the servo to a new ID
# 	"""
# 	pkt = Packet.makeWritePacket(curr_id, xl320.XL320_ID, [new_id])
# 	return pkt


def makeInterActive():
	# port = get_input('Enter serial port >> ')
	curr_id = get_input('Enter current id >> ')
	new_id = get_input('Enter new id >> ')
	return curr_id, new_id


def handleArgs():
	parser = argparse.ArgumentParser(description='set servo id')
	parser.add_argument('-i', '--interactive', help='input via commandline', action='store_true')
	parser.add_argument('-n', '--new_id', help='set new id', type=int, default=1)
	parser.add_argument('-c', '--current_id', help='current id', type=int, default=1)
	parser.add_argument('port', help='serial port', type=str)

	args = vars(parser.parse_args())
	return args


def main():
	args = handleArgs()

	if args['interactive']:
		port = args['port']
		curr_id, new_id = makeInterActive()
	else:
		port = args['port']
		curr_id = args['current_id']
		new_id = args['new_id']

	# create serial port
	ser = ServoSerial(port=port)
	ser.open()

	# create servo packet creator
	servo = Packet(pyservos.AX12)
	pkt = servo.makeWritePacket(curr_id, servo.base.ID, [new_id])
	print('pkt', pkt)

	ser.write(pkt)
	# if err:
	# 	print('Error: {} {}'.format(err, err_str))
	time.sleep(1)
	# ans = ser.read()
	# if ans:
	# 	print('Returned:', ans)
	# else:
	# 	print('No return')


if __name__ == '__main__':
	main()
