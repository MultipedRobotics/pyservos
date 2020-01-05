#!/usr/bin/env python

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################

from __future__ import print_function
from pyservos import Packet
from pyservos.servoserial import ServoSerial
import pyservos
from pyservos.utils import angle2int, le
import argparse


DESCRIPTION = """
Set the angle of a servo in degrees.

Example: set servo 3 to angle 45

./set_angle /dev/serial0 45 -i 3
"""

errorStr = {
    0: 'input voltage error',
    1: 'angle limit error',
    2: 'overheating error',
    3: 'range error',
    4: 'checksum error',
    5: 'overload error',
    6: 'instruction error'
}


def printErrorStr(pkt):
    if len(pkt) != 6:
        print('Bad packet: {}'.format(pkt))
    err = pkt[4]
    if err > 0:
        errs = []
        for i in range(7):
            if (err & (1 << i)):
                errs.append(errorStr[i])
        return errs
    return None


def handleArgs():
    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', '--id', help='servo id', type=int, default=0)
    parser.add_argument('port', help='serial port  or \'dummy\' for testing', type=str)
    parser.add_argument('angle', help='servo angle in degrees: 0.0 - 300.0', type=float)
    parser.add_argument('-t', '--type', help='type of servo, 1:AX-12A 2:XL-320 servo 3:XL-430, default: AX-12A', type=int, default=1)
    parser.add_argument('-s', '--speed', help='servo speed: 1 - 1023', type=int, default=0)

    args = vars(parser.parse_args())
    return args


def main():
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

    ID = args['id']
    port = args['port']
    angle = args['angle']
    speed = args['speed']

    print('Setting {} servo[{}] to {:.2f} on port {}'.format(servoStr[args['type']], ID, angle, port))

    serial = ServoSerial(port=port)
    serial.open()

    servo = Packet(servoType[args['type']])

    # pkt = servo.makeServoMovePacket(ID, angle)
    val = angle2int(angle, degrees=True) + le(speed)
    pkt = servo.makeWritePacket(ID, servo.base.GOAL_POSITION, val)
    ans = serial.sendPkt(pkt)  # send packet to servo
    if ans:
        print('status: {}'.format(ans))
        err = printErrorStr(ans)
        if err:
            print("Error ----------")
            for e in err:
                print(' >', e)


if __name__ == '__main__':
    main()
