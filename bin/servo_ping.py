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


def print_status_pkt(info, pkt):
	print('---------------------------------------')
	print("{:.<29} {}".format('id', info['id']))
	print("{}[{}]{:.<29} {}".format('Error', info['error num'], '', info['error str']))
	print('raw pkt: {}'.format(pkt))


def ping(port, rate, ID, retry=3):
	"""
	Sends a ping packet to ID's from 0 to maximum and prints out any returned
	messages.

	Actually send a broadcast and will retry (resend) the ping 3 times ...
	"""
	s = ServoSerial(port, rate)

	if ID < 0:
		ID = None

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
			pkts = servo.decodePacket(ans)
			for pkt in pkts:
				# servo = packetToDict(pkt)
				# utils.prettyPrintPacket(servo)
				info = servo.processStatusPacket(pkt)
				print_status_pkt(info, pkt)
		else:
			print('Try {}: no servos found'.format(cnt))

		time.sleep(0.1)

	s.close()


DESCRIPTION = """
Sends out a ping packet and prints all of the returned packets. If you don't
specify a specific id number, the program defaults to 'all'.

Example:

./servo_ping.py /dev/tty.usbserial-AL034G2K
Finding all servos:
Opened /dev/tty.usbserial-AL034G2K @ 1000000
---------------------------------------
id........................... 1
Firmware Ver................. 29
Model Number................. 350
Error........................ None
raw pkt: [255, 255, 253, 0, 1, 7, 0, 85, 0, 94, 1, 29, 31, 71]
---------------------------------------
id........................... 2
Firmware Ver................. 29
Model Number................. 350
Error........................ None
raw pkt: [255, 255, 253, 0, 2, 7, 0, 85, 0, 94, 1, 29, 21, 119]
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
	print('Finding all servos:')
	ping(port=args['port'], rate=args['rate'], ID=args['id'])
