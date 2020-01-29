##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
# Tests for continous integration

import pytest
from pyservos.utils import angle2int, le
from pyservos.xl320 import XL320
from math import pi


def packet_check(a, b):
    assert len(a) == len(b)
    for aa, bb in zip(a, b):
        # print(aa, bb)
        assert aa == bb


#####################################################
# XL-320 Tests
#####################################################

def test_error_packet():
    xl = XL320()

    pkt = [255, 255, 253, 0, 1, 4, 0, 85, 0, 161, 12]

    with pytest.raises(Exception):
        assert getPacketType(pkt) == 0x55
    # pkt = [255, 255, 253, 0, 1, 4, 0, 85, 128, 162, 143]
    # err_num, err_str = getErrorString(pkt)
    # assert err_num == 128  # this isn't right, but i don't understand it


def test_xl320_crc16():
    xl = XL320()
    pkt = [0xff, 0xff, 0xfd, 0x00, 0x01, 0x07, 0x00,  0x02, 0x63, 0x02, 0x04, 0x00, 0x1b, 0xf9]
    ans = xl.check_sum(pkt[:-2])  # you don't count the crc
    b = le(ans)
    assert b == [0x1b, 0xf9]


def test_xl320_find_pkts():
    xl = XL320()
    err = [0, 255, 255, 253, 0, 1, 4, 0, 85, 0, 161, 12, 0, 4, 0, 255, 255, 253, 0, 1, 4, 0, 85, 128, 162, 143, 0, 0]
    pkts = xl.decodePacket(err)
    assert len(pkts) == 2

    err = [0, 1, 4, 0, 85, 0, 161, 12, 0, 4, 0, 255, 255, 253]
    pkts = xl.decodePacket(err)
    assert len(pkts) == 0


# these compare built packages to correct packages
def test_xl320_reset_packet():
    xl = XL320()
    ans = [255, 255, 253, 0, 1, 4, 0, 6, 1, 161, 230]
    pkt = xl.makeResetPacket(1, 2)
    # print(ans)
    # print(pkt)
    packet_check(ans, pkt)


def test_xl320_ping_packet():
    xl = XL320()
    ans = [255, 255, 253, 0, 254, 3, 0, 1, 49, 66]
    pkt = xl.makePingPacket()
    packet_check(ans, pkt)


def test_xl320_reboot_packet():
    xl = XL320()
    ans = [255, 255, 253, 0, 1, 3, 0, 8, 47, 78]
    pkt = xl.makeRebootPacket(1)
    packet_check(ans, pkt)


def test_xl320_angle_packet():
    xl = XL320()
    ans = [255, 255, 253, 0, 1, 7, 0, 3, 30, 0, 139, 1, 83, 255]
    pkt = xl.makeServoMovePacket(1, 116)
    # print('\n')
    # print(ans)
    # print(pkt)
    packet_check(ans, pkt)


def test_xl320_led_packet():
    xl = XL320()
    ans = [255, 255, 253, 0, 1, 6, 0, 3, 25, 0, 1, 47, 98]
    pkt = xl.makeLEDPacket(1, XL320.LED_RED)
    # print(ans)
    # print(pkt)
    packet_check(ans, pkt)
