#!/usr/bin/env python3
from time import sleep
from serial import Serial
from pyservos.ax12 import AX12
from pyservos.servo_serial import ArduinoSerial
from colorama import Fore

# def send(serial, pkt):
#     pkts = bytearray(pkt)
#     bpkts = bytes(pkts)
#     serial.write(bpkts)
#     sleep(0.001)
#
# def get(serial, servo):
#     num = serial.in_waiting
#     if num > 0:
#         data = serial.read(num)
#         # for d in data:
#         #     print(int(d), end=',')
#         # print(" ")
#         d = list(bytearray(data))
#         dd = servo.decodePacket(d)
#         for d in dd:
#             print(servo.status_packet(d))
#     else:
#         print(f"{Fore.RED}Oops ... {Fore.RESET}")


port = "/dev/serial/by-id/usb-Adafruit_Trinket_M0_F42D3DEC504C5430372E314AFF090732-if00"

ser = ArduinoSerial(port)
ser.open()

servo = AX12()
val = 1
while True:
    val = 0 if val > 0 else 1
    # pkt = servo.makeWritePacket(1, 25, [val])
    pkt = servo.makeLEDPacket(AX12.BROADCAST_ADDR, val)
    ser.write(pkt)
    sleep(1)

# angles = [0, 150, 300, 150]

# rd = servo.makeReadAnglePacket(1)
# send(ser, rd)
# get(ser, servo)
#
# for a in angles:
#     pkt = servo.makeServoMovePacket(1, a)
#     send(ser, pkt)
#
#     sleep(0.01)
#     print(">> write: ", end='')
#     get(ser, servo)
#
#     sleep(1)
#
#     send(ser, rd)
#     print(f"{Fore.CYAN}>> read: ", end='')
#     get(ser, servo)
#     print(f"{Fore.RESET}")
