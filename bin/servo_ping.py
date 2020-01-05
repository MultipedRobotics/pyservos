#!/usr/bin/env python

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
# Send ping commands to all servos

from __future__ import print_function
from pyservos import Packet
from pyservos.servoserial import ServoSerial
import sys
import argparse
import time
import pyservos


# valid_return = False
# found_servos = {}


def print_status_pkt(info):
    print('---------------------------------------')
    print("{:.<29} {}".format('id', info['id']))
    print("{:.<29} {}".format('Error', info['error str']))
    print('raw pkt: {}'.format(info['raw']))


def ping(port, rate, ID, servoType, bcm_pin, retry=3):
    """
    Sends a ping packet to ID's from 0 to maximum and prints out any returned
    messages.

    Actually send a broadcast and will retry (resend) the ping 3 times ...
    """
    valid_return = False

    s = ServoSerial(port, rate, bcm_pin)

    if ID < 0:
        print('Pinging ALL servos')
        ID = None
    else:
        print('Pinging servo:', ID)

    try:
        s.open()
    except Exception as e:
        print('-'*40)
        print(sys.argv[0], ':')
        print(e)
        exit(1)

    servo = Packet(servoType)

    pkt = servo.makePingPacket(ID)
    s.write(pkt)

    found_servos = {}

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

        time.sleep(0.1)

    if valid_return:
        keys = list(found_servos.keys())
        keys.sort()

        for key in keys:
            print_status_pkt(found_servos[key])
    else:
        print('No servos found')

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
    parser.add_argument('-p', '--pin', help='Raspberry Pi GPIO BCM pin', type=int, default=-1)
    parser.add_argument('-t', '--type', help='type of servo, 1:AX-12A 2:XL-320 servo 3:XL-430, default: AX-12A', type=int, default=1)
    parser.add_argument('port', help='serial port name, set to "dummy" for testing', type=str)

    args = vars(parser.parse_args())
    return args


if __name__ == '__main__':
    args = handleArgs()
    servoType = {
        1: pyservos.AX12,
        2: pyservos.XL320,
        # 3: pyservos.XL430
    }
    servoStr = {
        1: 'AX-12A',
        2: 'XL-320',
        3: 'XL-430'
    }

    print('\nSearching for {} servos on {}\n'.format(servoStr[args['type']], args['port']))

    if args['pin'] > 0:
        pi_pin = args['pin']
    else:
        pi_pin = None

    ping(port=args['port'], rate=args['rate'], ID=args['id'], servoType=servoType[args['type']], bcm_pin=pi_pin)
