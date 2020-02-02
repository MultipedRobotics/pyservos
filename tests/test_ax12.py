##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
# Tests for continous integration
import pytest
from pyservos.utils import angle2int, le
from pyservos.ax12 import AX12
from math import pi


# def packet_check(a, b):
#     assert len(a) == len(b)
#     for aa, bb in zip(a, b):
#         # print(aa, bb)
#         assert aa == bb


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

#####################################################
# Uitilites and Misc
#####################################################

def test_angle2int():
    for angle in [0, 90, 180, 270, 300]:
        a = int(angle/300.0*1023.0)
        assert angle2int(angle, True) == le(a)

    for angle in [0, pi/4, pi/2, 3*pi/2]:
        a = int(180*angle/300.0/pi*1023.0)
        assert angle2int(angle, False) == le(a)

#####################################################
# AX-12 Tests
#####################################################
def test_ax12_find_packets():
    ax = AX12()

    # 2 good packets
    data = [
        0x3, 0x4,  # noise
        0xff, 0xff, 0x01, 0x04, 0x02, 0x2b, 0x01, 0xcc,
        0xff, 0xff,  # random header
        0xff, 0xff, 0xfe, 0x18, 0x83, 0x1e, 0x04, 0x00, 0x10, 0x00, 0x50, 0x01, 0x01, 0x20, 0x02, 0x60, 0x03, 0x02, 0x30, 0x00, 0x70, 0x01, 0x03, 0x20, 0x02, 0x80, 0x03, 0x12  # sync write
    ]

    ans = ax.find_packets(data)

    assert len(ans) == 2
    for a in ans:
        assert a


# @raises(Exception)
def test_ax12_fail_find_packets():
    ax = AX12()

    data = [
        0xff, 0xff,   # random header
        0xff, 0xff, 0x01, 0x04, 0x02, 0x2b, 0x01, 0x11  # bad packet, crc is wrong
    ]

    with pytest.raises(Exception):
        ans = ax.find_packets(data)

        assert len(ans) == 1
        for a in ans:
            assert a


def test_ax12_read_angle():
    ans = [255, 255, 1, 4, 2, 36, 2, 210]
    ax = AX12()
    pkt = ax.makeReadAnglePacket(1)
    assert pkt == ans, f"{pkt} != {ans}"

def test_ax12_check_sum():
    # data packets from:
    # http://support.robotis.com/en/product/actuator/dynamixel/communication/dxl_instruction.htm
    data = [
        [0xff, 0xff, 0x01, 0x04, 0x02, 0x2b, 0x01, 0xcc],  # read data
        [0xff, 0xff, 0xfe, 0x04, 0x03, 0x03, 0x1, 0xf6],  # write data
        [0xFF, 0xFF, 0x01, 0x02, 0x24, 0xD8],  # overload and over heat error
        [0xff, 0xff, 0x01, 0x02, 0x01, 0xfb],  # reg write
        [0xff, 0xff, 0x00, 0x02, 0x06, 0xf7],  # reset
        [0xff, 0xff, 0x01, 0x04, 0x02, 0x00, 0x03, 0xf5],  # read firmware
        [0xff, 0xff, 0x01, 0x02, 0x00, 0xfc],  # led status packet, no error
        [0xff, 0xff, 0xfe, 0x18, 0x83, 0x1e, 0x04, 0x00, 0x10, 0x00, 0x50, 0x01, 0x01, 0x20, 0x02, 0x60, 0x03, 0x02, 0x30, 0x00, 0x70, 0x01, 0x03, 0x20, 0x02, 0x80, 0x03, 0x12]  # sync write
    ]
    for d in data:
        cs = AX12.check_sum(d[2:-1])
        assert cs == d[-1]


def test_ax12_sync_write():
    ax = AX12()

    path = [
        # ID position velocity
        [0, 0x10, 0x00, 0x50, 0x01],
        [1, 0x20, 0x02, 0x60, 0x03],
        [2, 0x30, 0x00, 0x70, 0x01],
        [3, 0x20, 0x02, 0x80, 0x03]
    ]
    ans = [0xff, 0xff, 0xfe, 0x18, 0x83, 0x1e, 0x4, 0x0, 0x10, 0x0, 0x50, 0x1, 0x1, 0x20, 0x2, 0x60, 0x3, 0x2, 0x30, 0x0, 0x70, 0x1, 0x3, 0x20, 0x2, 0x80, 0x3, 0x12]
    pkt = ax.makeSyncWritePacket(AX12.GOAL_POSITION, path)
    # for p, a in zip(pkt, ans):
    #     assert p == a
    # packet_check(pkt, ans)
    assert pkt == ans, f"{ans} != {pkt}"


def test_ax12_bulk_read():
    ax = AX12()
    ans = [255, 255, 254, 11, 146, 2, 1, 36, 2, 2, 36, 2, 3, 36, 236]
    assert True

def test_ax12_angle_packet():
    ax = AX12()
    dpkt = ax.makeServoMovePacket(1, 116, degrees=True)
    # print(dpkt)
    rpkt = ax.makeServoMovePacket(1, 116*pi/180, degrees=False)
    # print(rpkt)
    # packet_check(dpkt, rpkt)
    assert dpkt == rpkt, f"{dpkt} != {rpkt}"

    ans = [255, 255, 1, 5, 3, 30, 255, 1, 216]
    pkt = ax.makeServoMovePacket(1, 150)
    assert ans == pkt, f"{ans} != {pkt}"

def test_ax12_ping_packet():
    ans = [255, 255, 254, 2, 1, 254]
    ax = AX12()
    pkt = ax.makePingPacket()

    assert pkt == ans, f"{pkt} != {ans}"


# @raises(Exception)
def test_ax12_led_fail():
    ax = AX12()

    with pytest.raises(Exception):
        ax.makeLEDPacket(2, 5)


#####################################################
# XL-320 Tests
#####################################################
#
# def test_error_packet():
#     xl = XL320()
#
#     pkt = [255, 255, 253, 0, 1, 4, 0, 85, 0, 161, 12]
#
#     with pytest.raises(Exception):
#         assert getPacketType(pkt) == 0x55
#     # pkt = [255, 255, 253, 0, 1, 4, 0, 85, 128, 162, 143]
#     # err_num, err_str = getErrorString(pkt)
#     # assert err_num == 128  # this isn't right, but i don't understand it
#
#
# def test_xl320_crc16():
#     xl = XL320()
#     pkt = [0xff, 0xff, 0xfd, 0x00, 0x01, 0x07, 0x00,  0x02, 0x63, 0x02, 0x04, 0x00, 0x1b, 0xf9]
#     ans = xl.base.check_sum(pkt[:-2])  # you don't count the crc
#     b = le(ans)
#     assert b == [0x1b, 0xf9]
#
#
# def test_xl320_find_pkts():
#     xl = XL320()
#     err = [0, 255, 255, 253, 0, 1, 4, 0, 85, 0, 161, 12, 0, 4, 0, 255, 255, 253, 0, 1, 4, 0, 85, 128, 162, 143, 0, 0]
#     pkts = xl.decodePacket(err)
#     assert len(pkts) == 2
#
#     err = [0, 1, 4, 0, 85, 0, 161, 12, 0, 4, 0, 255, 255, 253]
#     pkts = xl.decodePacket(err)
#     assert len(pkts) == 0
#
#
# # these compare built packages to correct packages
# def test_xl320_reset_packet():
#     xl = XL320()
#     ans = [255, 255, 253, 0, 1, 4, 0, 6, 1, 161, 230]
#     pkt = xl.makeResetPacket(1)
#     # print(ans)
#     # print(pkt)
#     packet_check(ans, pkt)
#
#
# def test_xl320_ping_packet():
#     xl = XL320()
#     ans = [255, 255, 253, 0, 254, 3, 0, 1, 49, 66]
#     pkt = xl.makePingPacket()
#     packet_check(ans, pkt)
#
#
# def test_xl320_reboot_packet():
#     xl = XL320()
#     ans = [255, 255, 253, 0, 1, 3, 0, 8, 47, 78]
#     pkt = xl.makeRebootPacket(1)
#     packet_check(ans, pkt)
#
#
# def test_xl320_angle_packet():
#     xl = XL320()
#     ans = [255, 255, 253, 0, 1, 7, 0, 3, 30, 0, 139, 1, 83, 255]
#     pkt = xl.makeServoMovePacket(1, 116)
#     # print('\n')
#     # print(ans)
#     # print(pkt)
#     packet_check(ans, pkt)
#
#
# def test_xl320_led_packet():
#     xl = XL320()
#     ans = [255, 255, 253, 0, 1, 6, 0, 3, 25, 0, 1, 47, 98]
#     pkt = xl.makeLEDPacket(1, XL320.LED_RED)
#     # print(ans)
#     # print(pkt)
#     packet_check(ans, pkt)
