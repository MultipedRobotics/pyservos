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
from lib import ping
from lib import set_id
from lib import set_angle
from lib import get_angle
from colorama import Fore, Back

# class _HelpAction(argparse._HelpAction):
#
#     def __call__(self, parser, namespace, values, option_string=None):
#         parser.print_help()
#
#         # retrieve subparsers from parser
#         subparsers_actions = [
#             action for action in parser._actions
#             if isinstance(action, argparse._SubParsersAction)]
#         # there will probably only be one subparser_action,
#         # but better save than sorry
#         for subparsers_action in subparsers_actions:
#             # get all subparsers and print help
#             for choice, subparser in subparsers_action.choices.items():
#                 print(f"{choice}: {subparser.format_usage()}")
#                 # print(subparser.format_help())
#                 # print(dir(subparser))
#                 # for line in subparser.format_help():
#                 #     print(line, end="")
#                 # print(subparser.format_usage())
#
#         parser.exit()

def handleArgs():
    parser = argparse.ArgumentParser(description='servo tool', add_help=True)
    # parser.add_argument('port', help='serial port', type=str)
    # parser.add_argument('--rate', help='serial port data rate', type=int, default=1000000)
    # parser.add_argument('-h','--help', action=_HelpAction, help='help for help if you need some help')  # add custom help

    subparsers = parser.add_subparsers()

    # Set Angle ---------------------------------------------------------------
    sa = subparsers.add_parser('angle', description="set servo angle")
    sa.add_argument('id', help='servo id [0-254]', type=int)
    sa.add_argument('angle', help='angle to set servo to [0-300] deg', type=float)
    sa.add_argument('--radians', help='optionally enter angle in radians', action='store_true')
    sa.set_defaults(which='set_angle')

    # Set ID ------------------------------------------------------------------
    si = subparsers.add_parser('id', description="set servo ID")
    # si.add_argument('-i', '--interactive', help='input via commandline', action='store_true')
    si.add_argument('current_id', help='current id', type=int)
    si.add_argument('new_id', help='set new id', type=int)
    si.set_defaults(which='set_id')

    # Ping --------------------------------------------------------------------
    p = subparsers.add_parser('ping', description="send ping")
    p.add_argument('--id', help='servo id to ping', type=int, default=254)
    p.set_defaults(which='ping')

    # Get Angle----------------------------------------------------------------
    ga = subparsers.add_parser('get', description="get servo angle")
    ga.add_argument('id', help='get servo angle', type=int)
    ga.set_defaults(which='get_angle')

    # Reboot ------------------------------------------------------------------
    rb = subparsers.add_parser('reboot', description="reboot a servo")
    rb.add_argument('id', help='reboot servo ID', type=int, default=254)
    rb.set_defaults(which='reboot')

    # Reset -------------------------------------------------------------------
    r = subparsers.add_parser('reset', description="reset servo")
    r.add_argument('id', help='get servo angle', type=int)
    r.add_argument('level', help="reset leve: 1-all, 2-all but ID, 3-all but ID and baudrate", type=int)
    r.set_defaults(which='reset')

    # Set Baudrate ------------------------------------------------------------
    b = subparsers.add_parser('baudrate', description="set servo baudrate")
    b.add_argument('baudrate', help='set servo baudrate', type=int)
    b.set_defaults(which='set_baudrate')

    parser.add_argument('port', help='serial port', type=str)
    parser.add_argument('--rate', help='serial port data rate', type=int, default=1000000)
    parser.add_argument('--dtr', help="set DTR pin for a Raspberry Pi", type=int)

    args = vars(parser.parse_args())
    return args


if __name__ == "__main__":

    args = handleArgs()
    print(args)

    if args['pi']:
        from pyservos.pi_servo_serial import PiServoSerial
        serial = PiServoSerial(args['port'], args['dtr'])
    else:
        serial = ServoSerial(args['port'])
    # try:
    #     serial.open()
    # except:
    #     print(Back.RED + "-------------------------")
    #     print(f" Invalid port: {args['port']}")
    #     print("-------------------------" + Back.RESET)
    #     exit(1)

    print(Back.GREEN + "="*80)
    print("| Servo AX-12A Tool")
    print(f"| serial port: {args['port']}  baudrate: {args['rate']}")
    print("-"*80 + Back.RESET)

    choice = args['which']
    if choice == "ping":
        print(f">> ping {args['id']}")
        ping(serial, args['id'])
    elif choice == "set_angle":
        angle = args['angle']
        if args['radians']:
            angle = angle*180/pi

        if 0 > angle > 300:
            raise Exception(f"Invalid angle: {angle}")
        print(f">> set servo[{args['id']}] angle: {angle}")
    elif choice == "set_id":
        print(f">> set servo[{args['id']}]: current: {args['current_id']} new: {args['new_id']}")
    elif choice == "get_angle":
        print(f">> get current angle from servo: {args['id']}")
    elif choice == "reboot":
        print(f">> reboot servo: {args['id']}")
    elif choice == "reset":
        print(f">> reset servo: {args['id']} to level: {args['level']}")
    # else:
    #     raise Exception("invalid commands")

    # print("-"*80)
