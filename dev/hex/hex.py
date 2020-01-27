#!/usr/bin/env python

from pyservos.ax12 import AX12
from pyservos.servo_serial import ServoSerial
import yaml
import time

class Tripod:
    def __init__(self):
        self.build_gait()

    def build_gait(self):
        """This gait is all in angular space"""
        # z movement
        d = 200
        r = d + 5
        l = 150
        # x-y movement
        dd = 40
        f = 150-dd
        b = 150+dd
        m = 150

        self.gait = [
            [r,d,l,d,r,r,r,r], # servo 1 (tibia)
            [f,f,m,b,b,b,m,f]  # servo 2 (hip)
        ]
        self.cycle = len(self.gait[0])

    def __getitem__(self, i):
        i = i % self.cycle
        return (self.gait[0][i], self.gait[1][i],)

    def __len__(self):
        return self.cycle


if __name__ == "__main__":
    gait = Tripod()
    servo = AX12()

    port = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A904MISU-if00-port0"
    serial = ServoSerial(port)
    serial.open()

    try:
        while True:
            for i in range(len(gait)):
                print(f">> gait[{i}] = {gait[i]}")
                s2, s1 = gait[i]
                pkt1 = servo.makeServoMovePacket(1, s1, degrees=True)
                pkt2 = servo.makeServoMovePacket(2, s2, degrees=True)
                serial.sendPkt(pkt1)
                serial.sendPkt(pkt2)
                time.sleep(0.5)

    except KeyboardInterrupt:
        pass
