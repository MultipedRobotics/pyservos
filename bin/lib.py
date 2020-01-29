#!/usr/bin/env python
from pyservos.ax12 import AX12
# from pyservos.servoserial import ServoSerial
# import sys
import argparse
import time
from colorama import Fore, Back
# import pyservos
from colorama import Fore, Back
import platform  # system info
from math import pi



def print_status_pkt(info):
    print('---------------------------------------')
    print("{:.<29} {}".format('id', info['id']))
    if info['error str'] == "None":
        print(Fore.GREEN + "{:.<29} {}".format('Error', info['error str']) + Fore.RESET)
    else:
        print(Fore.RED + "{:.<29} {}".format('Error', info['error str']) + Fore.RESET)
    print('raw pkt: {}'.format(info['raw']))

def ping(serial, id):
    """
    Sends a ping packet to ID's from 0 to maximum and prints out any returned
    messages.

    Actually send a broadcast and will retry (resend) the ping 3 times ...
    """
    # port = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A904MISU-if00-port0"
    retry = 3
    valid_return = False

    # s = ServoSerial(port)  # FIXME
    s = serial
    s.open()

    # try:
    #     s.open()
    # except Exception as e:
    #     print('-'*40)
    #     print(sys.argv[0], ':')
    #     print(e)
    #     exit(1)

    servo = AX12()

    pkt = servo.makePingPacket(id)
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


def loop(serial, servo):
    while True:
        choice = input("<<")
        c = choice.split(' ')
        # a = {'which': c[0], 'args': c[1:]}
        print(f">> {c}")

        args = handleArgs(string = c)
        print("argparse: {args}")

        if choice == "q":
            break


def handleArgs(string=None):
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
    r.add_argument('level', help="reset leve: 1-all, 2-all but ID, 3-all but ID and baudrate", type=int, default=3)
    r.set_defaults(which='reset')

    # Set Baudrate ------------------------------------------------------------
    b = subparsers.add_parser('baudrate', description="set servo baudrate")
    b.add_argument('baudrate', help='set servo baudrate', type=int)
    b.set_defaults(which='set_baudrate')

    l = subparsers.add_parser('loop', description="loop")
    l.set_defaults(which='loop')

    # Main Servo --------------------------------------------------------------
    parser.add_argument('port', help='serial port', type=str)
    parser.add_argument('--rate', help='serial port data rate', type=int, default=1000000)
    parser.add_argument('--dtr', help="set DTR pin for a Raspberry Pi", type=int)
    parser.add_argument('-d', '--debug', help="print debugging info", action="store_true")
    # parser.add_argument('--loop', help="enter an interactive session", action="store_true")

    if string:
        parser.parse_args(string)

    args = vars(parser.parse_args())
    return args
