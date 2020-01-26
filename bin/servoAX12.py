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
    p = subparsers.add_parser('get', description="get servo angle")
    p.add_argument('id', help='get servo angle', type=int)
    p.set_defaults(which='get_angle')

    parser.add_argument('port', help='serial port', type=str)
    parser.add_argument('--rate', help='serial port data rate', type=int, default=1000000)

    args = vars(parser.parse_args())
    return args


if __name__ == "__main__":

    args = handleArgs()
    print(args)

    serial = ServoSerial(args['port'])

    print("="*80)
    print("| Servo AX-12A Tool")
    print(f"| serial port: {args['port']}  baudrate: {args['rate']}")
    print("-"*80)
    choice = args['which']
    if choice == "ping":
        print(f">> ping {args['id']}")
        ping(serial, args['id'])
    elif choice == "set_angle":
        angle = args['angle']
        if args['radians']:
            angle = angle*180/pi
        print(f">> set servo[{args['id']}] angle: {angle}")
    elif choice == "set_id":
        print(f">> set servo[{args['id']}]: current: {args['current_id']} new: {args['new_id']}")
    elif choice == "get_angle":
        print(f">> get current angle from servo: {args['id']}")

    # print("-"*80)
