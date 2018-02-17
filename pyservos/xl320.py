##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################

from __future__ import division
from __future__ import print_function


class XL320(object):
	SERVO_ID = 2

	def __init__(self):
		print('<<< WARNING: this is not setup yet >>>')

	def check_sum(self, pkt):
		return 25

	def header(self, ID):
		return [0xff, 0xff, 0x00, 0xdf, ID]

	def led(self, value):
		return [1, 2, 3]
