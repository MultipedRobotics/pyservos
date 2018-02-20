# ##############################################
# # The MIT License (MIT)
# # Copyright (c) 2016 Kevin Walchko
# # see LICENSE for full details
# ##############################################
#


from __future__ import division
from __future__ import print_function
# from .utils import le, angle2int


class AX12(object):
	"""
	This class handles the AX-12A servo using Dynimel's Protocol version 1.0.
	"""
	SERVO_ID = 1

	# --------- INSTRUCTIONS -----
	PING      = 0x01
	READ      = 0x02
	WRITE     = 0x03
	REG_WRITE = 0x04
	ACTION    = 0x05
	RESET     = 0x06
	# REBOOT    = 0x08
	# STATUS    = 0x55
	# SYNC_READ  = 0x82
	SYNC_WRITE = 0x83
	BULK_READ  = 0x92
	# BULK_WRITE = 0x93

	# -------- EEPROM -------------
	MODEL_NUMBER    = 0
	VER_FIRMWARE    = 2
	ID              = 3
	BAUD_RATE       = 4
	DELAY_TIME      = 5
	CW_ANGLE_LIMIT  = 6   # min angle, default 0
	CCW_ANGLE_LIMIT = 8   # max angle, default 300
	CONTROL_MODE    = 11  # joint or wheel mode, default joint (servo)
	MAX_TORQUE      = 15
	RETURN_LEVEL    = 17

	# -------- RAM ----------------
	TORQUE_ENABLE    = 24  # servo mode on/off - turn into wheel
	LED              = 25
	GOAL_POSITION    = 30
	GOAL_VELOCITY    = 32
	GOAL_TORQUE      = 35
	PRESENT_POSITION = 37  # current servo angle
	PRESENT_SPEED    = 39  # current speed
	PESENT_LOAD      = 41  # current load
	PESENT_VOLTAGE   = 45  # current voltage
	PESENT_TEMP      = 46  # current temperature
	MOVING           = 49
	HW_ERROR_STATUS  = 50
	PUNCH            = 51

	# --------- OTHER -------------
	RESET_ALL                  = 0xFF
	RESET_ALL_BUT_ID           = 0x01
	RESET_ALL_BUT_ID_BAUD_RATE = 0x02
	LED_ON                     = 1
	LED_OFF                    = 0
	BROADCAST_ADDR             = 0xfe  # a packet with this ID will go to all servos
	WHEEL_MODE                 = 1
	JOINT_MODE                 = 2  # normal servo
	DR_1000000                 = 1  # bps = 2000000/(data + 1)

	def __init__(self):
		pass

	@staticmethod
	def check_sum(data):
		"""
		checksum = 255 - ((id + length + data1 + data2 + ... + dataN) & 255)
		"""
		# print(data)
		return 255 - (sum(data) & 255)

	def makePacket(self, ID, instr, params=None):
		"""
		This makes a generic packet.

		0xFF, 0xFF, ID, LENGTH, INST, PARAM 1, PARAM 2, ..., PARAM N, CHECKSUM]
		in:
			ID - servo id
			instr - instruction
			params - instruction parameter values
		out: packet
		"""
		pkt = [0xff, 0xff, ID]
		if params:
			# print(params)
			length = len(params) + 2
			pkt += [length, instr]
			pkt += params
			# print(self.check_sum(pkt[2:]))
			pkt += [self.check_sum(pkt[2:])]
		else:
			pkt += [2, instr, self.check_sum([ID, 2, instr])]

		return pkt

	def find_packets(self, pkt):
		"""
		Search through a string of binary for a valid ax-12 package.

		in: buffer to search through
		out: a list of valid data packet
		"""
		# print('findpkt', pkt)
		# print('-----------------------')
		ret = []
		while len(pkt)-6 >= 0:
			try:
				# print(pkt)
				# check for header
				if pkt[0:2] != [0xFF, 0xFF]:
					pkt.pop(0)  # get rid of the first index
					continue
				length = pkt[3]  # get length
				crc_pos = 3 + length
				pkt_crc = pkt[crc_pos]  # packet crc
				crc = self.check_sum(pkt[2:crc_pos])  # calculated crc
				if pkt_crc == crc:
					pkt_end = crc_pos+1
					ret.append(pkt[:pkt_end])
					del pkt[:pkt_end]
				else:
					pkt.pop(0)
			except Exception:
				pkt.pop(0)
		return ret

	def status_packet(self, pkt):
		def getError(err):
			errors = [
				'Input Voltage',  # 0
				'Angle Limit',
				'Overheating',
				'Range',
				'Checksum',
				'Overload',
				'Instrunction',
				'None'  # 7
			]
			# ret = None
			if not (err == 128 or err == 0):
				err_str = []
				for i in range(0, 8):
					if (err >> i) & 1:
						err_str.append(errors[i])
				ret = ','.join(err_str)
			else:
				ret = errors[7]
			return ret

		ret = {
			'id': pkt[2],
			'error str': getError(pkt[4]),
			'error num': pkt[4],
			'params': pkt[5:-1],
			'raw': list(pkt)
		}
		return ret
