###############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################

from __future__ import division
from __future__ import print_function
from .ax12 import AX12
from .xl320 import XL320
from .utils import angle2int, le


# def le(h):
# 	"""
# 	Little-endian, takes a 16b number and returns an array arrange in little
# 	endian or [low_byte, high_byte].
# 	"""
# 	h &= 0xffff  # make sure it is 16 bits
# 	return [h & 0xff, h >> 8]
#
#
# def angle2int(angle, degrees=True):
# 	if degrees:
# 		angle = le(int(angle/300*1023))  # degrees
# 	else:
# 		angle = le(int(angle/5.23598776*1023))  # radians
# 	return angle


# PacketManager
# PacketSystem
# Packet
class Packet(object):
	"""
	This is a wrapper class for the xl-320 and ax-12 servos. It can only talk
	to one servo type at a time.
	"""

	def __init__(self, kind):
		self.base = kind()

	def makePingPacket(self, ID=None):
		"""
		Pings a servo
		"""
		if not ID:
			ID = self.base.BROADCAST_ADDR
		pkt = self.base.makePacket(ID, self.base.PING)
		return pkt

	def makeWritePacket(self, ID, reg, values=None):
		"""
		Creates a packet that writes a value(s) to servo ID at location reg. Make
		sure the values are in little endian (use Packet.le() if necessary) for 16 b
		(word size) values.
		"""
		if values:
			if self.base.SERVO_ID == XL320.SERVO_ID:
				params = le(reg) + values
			else:
				params = [reg] + values
		else:
			if self.base.SERVO_ID == XL320.SERVO_ID:
				params = le(reg)
			else:
				params = [reg]

		pkt = self.base.makePacket(ID, self.base.WRITE, params)
		return pkt

	def makeReadPacket(self, ID, reg, values=None):
		"""
		Creates a packet that reads the register(s) of servo ID at location reg. Make
		sure the values are in little endian (use Packet.le() if necessary) for 16 b
		(word size) values.
		"""
		pkt = self.base.makePacket(ID, self.base.READ, [reg, values])
		return pkt

	def makeResetPacket(self, ID, level=0):
		"""
		Resets a servo.
		"""
		if self.base.SERVO_ID == XL320.SERVO_ID:
			params = [XL320.RESET_ALL_BUT_ID]
		else:
			params = None

		pkt = self.base.makePacket(ID, self.base.RESET, params)
		return pkt

	def makeRebootPacket(self, ID):
		"""
		Reboots a servo
		"""

		pkt = self.base.makePacket(ID, self.base.REBOOT)
		return pkt

	def makeServoMovePacket(self, ID, angle, degrees=True):
		"""
		Commands the servo to an angle (in degrees)
		"""
		# if degrees and not (0.0 <= angle <= 300.0):
		# 	raise Exception('makeServoMovePacket(), angle [deg] out of bounds: {}'.format(angle))
		# elif (not degrees) and (not (0.0 <= angle <= 5.23598776)):
		# 	raise Exception('makeServoMovePacket(), angle [rads] out of bounds: {}'.format(angle))
		# val = int(angle/300*1023)
		val = angle2int(angle, degrees)

		pkt = self.makeWritePacket(ID, self.base.GOAL_POSITION, val)
		return pkt

	def makeSyncMovePacket(self, info, degrees=True):
		"""
		Write sync angle information to servos.

		info = [[ID, angle], [ID, angle], ...]
		ID: servo ID
		angle: 0-300 degrees or in radians
		"""
		data = []

		# since all servo angles have the same register addr (GOAL_POSITION)
		# and data size (2), a sinc packet is smart choice
		# compare bulk vs sync for the same commands:
		# bulk = 94 bytes
		# sync = 50 bytes
		for cmd in info:
			data.append(cmd[0])  # ID
			angle = angle2int(cmd[1], degrees)
			data.append(angle[0])  # LSB
			data.append(angle[1])  # MSB

		pkt = self.makeSyncWritePacket(self.base.GOAL_POSITION, data)
		return pkt

	def makeSyncWritePacket(self, reg, info):
		"""
		Write sync angle information to servos.

		info = [[ID, data1, ...], [ID, data1, ...], ...]
		"""
		data = []
		data.append(reg)  # addr
		# length = (len(info[0])+1)*(len(info)+4)
		# data.append(length)  # data length
		data.append(len(info[0])-1)
		for cmd in info:
			data += cmd

		ID = self.base.BROADCAST_ADDR
		instr = self.base.SYNC_WRITE
		pkt = self.base.makePacket(ID, instr, data)  # create packet
		return pkt

	def makeBulkReadPacket(self, data):
		"""
		data = [[data len, ID, addr], [data len, ID, addr], ...]
		"""
		ID = self.base.BROADCAST_ADDR
		instr = self.base.BULK_READ
		pkt = self.base.makePacket(ID, instr, data)  # create packet
		return pkt

	def makeLEDPacket(self, ID, value):
		"""
		Turn on/off the servo LED and also sets the color.
		"""
		if self.base.SERVO_ID == AX12.SERVO_ID:
			if value < 0 or value > 1:
				raise Exception("ERROR: LED can only be off or on: {}".format(value))
			# value = [value]
		# elif self.base.SERVO_ID == XL320.SERVO_ID:
		# 	# print('Not implemented yet')
		# 	value = [0, value]

		pkt = self.makeWritePacket(ID, self.base.LED, [value])
		return pkt

	def decodePacket(self, pkts):
		return self.base.find_packets(pkts)

	def processStatusPacket(self, pkt):
		return self.base.status_packet(pkt)
