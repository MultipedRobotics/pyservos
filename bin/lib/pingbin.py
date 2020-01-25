#!/usr/bin/env python
from ax12 import AX12
from pyservos.servoserial import ServoSerial
import sys
import argparse
import time
from colorama import Fore, Back
# import pyservos



def print_status_pkt(info):
    print('---------------------------------------')
    print("{:.<29} {}".format('id', info['id']))
    if info['error str'] == "None":
        print(Fore.GREEN + "{:.<29} {}".format('Error', info['error str']) + Fore.RESET)
    else:
        print(Fore.RED + "{:.<29} {}".format('Error', info['error str']) + Fore.RESET)
    print('raw pkt: {}'.format(info['raw']))

def ping(serial):
    """
    Sends a ping packet to ID's from 0 to maximum and prints out any returned
    messages.

    Actually send a broadcast and will retry (resend) the ping 3 times ...
    """
    # port = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A904MISU-if00-port0"
    retry = 3
    valid_return = False

    s = serial  # FIXME

    # try:
    #     s.open()
    # except Exception as e:
    #     print('-'*40)
    #     print(sys.argv[0], ':')
    #     print(e)
    #     exit(1)

    servo = AX12()

    pkt = servo.makePingPacket(None)
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


# ping()
