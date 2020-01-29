##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
# Tests for continous integration

import pytest
from pyservos.servo_serial import ServoSerial


def packet_check(a, b):
    assert len(a) == len(b)
    for aa, bb in zip(a, b):
        # print(aa, bb)
        assert aa == bb


# #####################################################
# # Serial Tests
# #####################################################
# def test_fake_serial():
#     s = ServoSerial('/dev/null')
#     s.open()
#     msg = [71, 72, 73]  # ascii: GHI
#     s.write(msg)
#     ret = s.read()
#     for r, m in zip(ret, msg):
#         print(r, m)
#         assert r == m
#
#     s.write(msg)
#     s.flushInput()  # destroy input, ret should be empty now
#     ret = s.read()
#     assert len(ret) == 0
#
#     s.close()
