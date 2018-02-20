#!/usr/bin/env python

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
# Send ping commands to all servos

from __future__ import print_function
from pyservos import Packet
from pyservos import ServoSerial
import sys
import argparse
import time
import pyservos


valid_return = False
found_servos = {}


def print_status_pkt(info):
	print('---------------------------------------')
	print("{:.<29} {}".format('id', info['id']))
	print("{:.<29} {}".format('Error', info['error str']))
	print('raw pkt: {}'.format(info['raw']))


def ping(port, rate, ID, retry=3):
	"""
	Sends a ping packet to ID's from 0 to maximum and prints out any returned
	messages.

	Actually send a broadcast and will retry (resend) the ping 3 times ...
	"""
	global valid_return

	s = ServoSerial(port, rate)

	if ID < 0:
		print('Pinging ALL servos')
		ID = None
	else:
		print('Pinging servo:', ID)

	try:
		s.open()
	except Exception as e:
		# print('Error opening serial port:')
		print('-'*40)
		print(sys.argv[0], ':')
		print(e)
		exit(1)

	servo = Packet(pyservos.AX12)

	pkt = servo.makePingPacket(ID)
	# print('ping', pkt)
	s.write(pkt)

	# as more servos add up, I might need to increase the cnt number???
	for cnt in range(retry):
		ans = s.read()

		if ans:
			valid_return = True
			pkts = servo.decodePacket(ans)
			for pkt in pkts:
				info = servo.processStatusPacket(pkt)
				if info['id'] not in found_servos.keys():
					found_servos[info['id']] = info
				# print_status_pkt(info, pkt)
		else:
			if not valid_return:
				print('Try {}: no servos found'.format(cnt))

		time.sleep(0.1)

	keys = found_servos.keys()
	keys.sort()

	for key in keys:
		print_status_pkt(found_servos[key])

	s.close()


DESCRIPTION = """
Sends out a ping packet and prints all of the returned packets. If you don't
specify a specific id number, the program defaults to 'all'.

Example:

kevin@logan bin $ ./servo_ping.py /dev/tty.usbserial-AL034G1T
Finding all servos:
Opened /dev/tty.usbserial-AL034G1T @ 1000000
Try 0: no servos found
---------------------------------------
id........................... 1
Error........................ None
raw pkt: [255, 255, 1, 2, 0, 252]
"""


def handleArgs():
	parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-r', '--rate', help='servo baud rate', type=int, default=1000000)
	parser.add_argument('-i', '--id', help='ping servo ID', type=int, default=-1)
	parser.add_argument('port', help='serial port name, set to "dummy" for testing', type=str)

	args = vars(parser.parse_args())
	return args


if __name__ == '__main__':
	args = handleArgs()
	ping(port=args['port'], rate=args['rate'], ID=args['id'])
