#!/usr/bin/env python

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
# ----------------------------
# Simple tool to work with AX-12 servos
#

from pyservos.ax12 import AX12
from pyservos.servo_serial import ServoSerial
# import sys
import argparse
import time
from math import pi
# from lib import ping
# from lib import set_id
# from lib import set_angle
# from lib import get_angle
from .lib import loop, handleArgs, ping
from colorama import Fore, Back
import platform  # system info


# def handleArgs(string=None):
#     parser = argparse.ArgumentParser(description='servo tool', add_help=True)
#     # parser.add_argument('port', help='serial port', type=str)
#     # parser.add_argument('--rate', help='serial port data rate', type=int, default=1000000)
#     # parser.add_argument('-h','--help', action=_HelpAction, help='help for help if you need some help')  # add custom help
#
#     subparsers = parser.add_subparsers()
#
#     # Set Angle ---------------------------------------------------------------
#     sa = subparsers.add_parser('angle', description="set servo angle")
#     sa.add_argument('id', help='servo id [0-254]', type=int)
#     sa.add_argument('angle', help='angle to set servo to [0-300] deg', type=float)
#     sa.add_argument('--radians', help='optionally enter angle in radians', action='store_true')
#     sa.set_defaults(which='set_angle')
#
#     # Set ID ------------------------------------------------------------------
#     si = subparsers.add_parser('id', description="set servo ID")
#     # si.add_argument('-i', '--interactive', help='input via commandline', action='store_true')
#     si.add_argument('current_id', help='current id', type=int)
#     si.add_argument('new_id', help='set new id', type=int)
#     si.set_defaults(which='set_id')
#
#     # Ping --------------------------------------------------------------------
#     p = subparsers.add_parser('ping', description="send ping")
#     p.add_argument('--id', help='servo id to ping', type=int, default=254)
#     p.set_defaults(which='ping')
#
#     # Get Angle----------------------------------------------------------------
#     ga = subparsers.add_parser('get', description="get servo angle")
#     ga.add_argument('id', help='get servo angle', type=int)
#     ga.set_defaults(which='get_angle')
#
#     # Reboot ------------------------------------------------------------------
#     rb = subparsers.add_parser('reboot', description="reboot a servo")
#     rb.add_argument('id', help='reboot servo ID', type=int, default=254)
#     rb.set_defaults(which='reboot')
#
#     # Reset -------------------------------------------------------------------
#     r = subparsers.add_parser('reset', description="reset servo")
#     r.add_argument('id', help='get servo angle', type=int)
#     r.add_argument('level', help="reset leve: 1-all, 2-all but ID, 3-all but ID and baudrate", type=int, default=3)
#     r.set_defaults(which='reset')
#
#     # Set Baudrate ------------------------------------------------------------
#     b = subparsers.add_parser('baudrate', description="set servo baudrate")
#     b.add_argument('baudrate', help='set servo baudrate', type=int)
#     b.set_defaults(which='set_baudrate')
#
#     l = subparsers.add_parser('loop', description="loop")
#     l.set_defaults(which='loop')
#
#     # Main Servo --------------------------------------------------------------
#     parser.add_argument('port', help='serial port', type=str)
#     parser.add_argument('--rate', help='serial port data rate', type=int, default=1000000)
#     parser.add_argument('--dtr', help="set DTR pin for a Raspberry Pi", type=int)
#     parser.add_argument('-d', '--debug', help="print debugging info", action="store_true")
#     # parser.add_argument('--loop', help="enter an interactive session", action="store_true")
#
#     if string:
#         parser.parse_args(string)
#
#     args = vars(parser.parse_args())
#     return args


def main():

    servo = AX12()

    args = handleArgs()

    # check for common errors
    if 'level' in args:
        if args['level'] not in [1,2,3]:
            print(f"Invalid level: {args['level']}")
            # print(args)
            print(Fore.RED + str(args) + Fore.RESET)
            exit(1)

    if 'id' in args:
        if not (1 <= args['id'] <= 254):
            print(f"Invalid ID: {args['id']}")
            # print(args)
            print(Fore.RED + str(args) + Fore.RESET)
            exit(1)

    if args['debug']:
        print(Fore.YELLOW + str(args) + Fore.RESET)

    # create a serial port
    if args['dtr']:
        from pyservos.pi_servo_serial import PiServoSerial
        serial = PiServoSerial(args['port'], args['dtr'])
    else:
        serial = ServoSerial(args['port'])

    # try to open serial port
    try:
        serial.open()
    except:
        print(Back.RED + "-------------------------")
        print(f" Invalid port: {args['port']}")
        print("-------------------------" + Back.RESET)
        exit(1)

    # Print serial open success!!!
    uname = platform.uname()
    print(Back.GREEN + "="*80)
    # print("| Servo AX-12A Tool")
    print(f"| {uname.node}:{uname.system}")
    print(f"| Python {platform.python_version()}")
    print(f"| baudrate: {args['rate']}")
    print(f"| serial port: {args['port']}")
    print("-"*80 + Back.RESET)

    # servo = AX12()

    choice = args['which']
    if choice == "ping":
        print(f">> ping {args['id']}")
        ping(serial, args['id'])

    elif choice == "set_angle":
        if 'angle' not in args or 'id' not in args:
            raise Exception("Invalid input")

        angle = args['angle']
        if args['radians']:
            angle = angle*180/pi

        if not (0 <= angle <= 300):
            raise Exception(f"Invalid angle: {angle}")

        print(f">> set servo[{args['id']}] angle: {angle}")

        pkt = servo.makeServoMovePacket(args['id'], angle)
        serial.sendPkt(pkt)

    elif choice == "set_id":
        if 'current_id' not in args or 'new_id' not in args:
            print("Invalid input")
            exit(1)
        if 0 > args['new_id'] > 253:
            print("Invalid ID number, must be between 0-253")
            exit(1)
        print(f">> set servo[{args['current_id']}] to new ID: {args['new_id']}")
        pkt = servo.makeSetIDPacket(args['current_id'], args['new_id'])
        serial.write(pkt)

    elif choice == "get_angle":
        # print(Fore.RED + "Not currently implemented" + Fore.RESET)
        print(f">> get current angle from servo: {args['id']}")
        pkt = servo.makeReadAnglePacket(args['id'])
        # pkt = servo.makeServoInfoPacket(args['id'])
        # d = [
        #     # [data len, ID, addr]
        #     [2, 1, servo.PRESENT_POSITION],
        #     # [2, 2, servo.PRESENT_POSITION],
        #     # [2, 3, servo.PRESENT_POSITION],
        # ]
        # pkt = servo.makeBulkReadPacket(d)
        # print(pkt)
        ans = serial.sendPkt(pkt)
        # print(Fore.BLUE + str(ans) + Fore.RESET)
        # print("<<", ans)

        ans = servo.find_packets(ans)
        if ans:
            # print(ans[0])
            ans = ans[0]
            err = ans[4]
            angle = (ans[6]<<8) + ans[5]
            deg = angle * 300/1023
            print(f">> Angle: {angle} cnts {deg} deg")

    elif choice == "reboot":
        print(f">> reboot servo: {args['id']}")
        pkt = servo.makeRebootPacket(args['id'])
        serial.write(pkt)

    elif choice == "reset":
        print(f">> reset servo: {args['id']} to level: {args['level']}")
        if args['level'] not in [1,2,3]:
            print(Fore.RED + "Invalid input" + Fore.RESET)
            exit(1)
        pkt = servo.makeResetPacket(args['id'], args['level'])
        serial.write(pkt)
    # elif args['loop']:
    elif choice == "loop":
        loop(serial, servo)

    serial.close()


if __name__ == "__main__":
    main()
