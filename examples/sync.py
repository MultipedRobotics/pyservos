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

# http://support.robotis.com/en/product/actuator/dynamixel/communication/dxl_instruction.htm
# http://support.robotis.com/en/

def main():

	port = "/dev/tty.usbserial-AL034G1T"

	serial = ServoSerial(port=port)
	serial.open()

	servo = Packet(pyservos.AX12)
	# servo = Packet(pyservos.XL320)

	# build
	# 59 rpm max
	data = []
	ids = [1, 2, 3]
	pos = [150, 200, 90]
	vel = [200, 100, 300]  # 0.111 rpm

	for i, p, v in zip(ids, pos, vel):
		data.append([i] + angle2int(p) + le(v))

	pkt = servo.makeSyncWritePacket(pyservos.AX12.GOAL_POSITION, data)
	print(pkt)

	ans = serial.sendPkt(pkt)  # send packet to servo
	ans = servo.processStatusPacket(ans)

	if ans:
		print('status: {}'.format(ans))


main()


#
# from __future__ import print_function
# from __future__ import division
# from pyxl320.Packet import makeSyncAnglePacket
# from pyxl320 import ServoSerial
# from pyxl320 import DummySerial
# import argparse
#
#
# def handleArgs():
# 	parser = argparse.ArgumentParser(description='set servos to an angle using sync command')
# 	parser.add_argument('angle', help='servo angle', type=float, default=150.0)
# 	parser.add_argument('-p', '--port', help='serial port', type=str, default='/dev/serial0')
# 	# parser.add_argument('-g', '--gpio', help='Raspberry Pi GPIO pin number', type=int, default=17)
#
# 	args = vars(parser.parse_args())
# 	return args
#
#
# args = handleArgs()
# port = args['port']
# angle = args['angle']
#
# if port:
# 	print('Opening: {}'.format(port))
# 	serial = ServoSerial(port)  # use this if you want to talk to real servos
# else:
# 	print('Using dummy serial port for testing')
# 	serial = DummySerial(port)  # use this for simulation
#
# serial.open()
#
# data = [
# 	(1, angle),
# 	(2, angle),
# 	(3, angle),
#
# 	(4, angle),
# 	(5, angle),
# 	(6, angle),
#
# 	(7, angle),
# 	(8, angle),
# 	(9, angle),
#
# 	(10, angle),
# 	(11, angle),
# 	(12, angle)
# ]
#
# pkt = makeSyncAnglePacket(data)
# serial.sendPkt(pkt)
#
# serial.close()
