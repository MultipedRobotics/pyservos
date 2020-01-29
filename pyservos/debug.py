##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################

class Debug(object):
	"""
	Not sure about the value of this ...
	"""

	# def packetToDict(pkt):
	# 	"""
	# 	Given a packet, this turns it into a dictionary ... is this useful?
    #
	# 	in: packet, array of numbers
	# 	out: dictionary (key, value)
	# 	"""
    #
	# 	d = {
	# 		'id': pkt[4],
	# 		# 'instruction': xl320.InstrToStr[pkt[7]],
	# 		# 'length': (pkt[6] << 8) + pkt[5],
	# 		# 'params': pkt[8:-2],
	# 		'Model Number': (pkt[10] << 8) + pkt[9],
	# 		'Firmware Ver': pkt[11],
	# 		# 'Error': ErrorStatusMsg[pkt[8]],
	# 		# 'crc': pkt[-2:]
	# 	}
    #
	# 	return d

	def hex_decode(self, data):
		"""
		Takes an array of number and turns them into a string of hex for printing.

		in: data - array of numbers [1,2,33,42,234]
		out: str - '0x1 0x02 0x21 0x2a 0xea'
		"""
		return ''.join(map('0x{:02X} '.format, data))

	def prettyPrintPacket(self, ctrl_table):
		"""
		This will pretty print out a packet's fields.

		in: dictionary of a packet
		out: nothing ... everything is printed to screen
		"""
		print('---------------------------------------')
		print("{:.<29} {}".format('id', ctrl_table['id']))
		ctrl_table.pop('id')
		for key, value in ctrl_table.items():
			print("{:.<29} {}".format(key, value))
