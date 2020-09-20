##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################
# List - return type
# Sequence - arg type
from typing import Sequence, Union, List
import serial as PySerial # type: ignore
import time
from colorama import Fore
# import pty

class ArduinoSerial:
    """
    Use this with the USB to Dynamixel serial port. This makes it easier for
    computers that can't do 1Mbps (looking at you fucking macOS) nicely.
    """
    def __init__(self, port, baud_rate=11520):
        self.serial = PySerial.Serial()
        self.serial.baudrate = baud_rate
        self.serial.port = port

    def __del__(self) -> None:
        """
        Destructor: closes the serial port
        """
        self.close()

    def open(self):
        if self.serial.is_open:
            return True

        self.serial.open()

        # self.setRTS(self.DD_WRITE)
        if self.serial.isOpen():
            # print('Opened {} @ {}'.format(self.serial.name, self.serial.baudrate))
            # print(self.serial.get_settings())
            return True

        return False
        # else:
        #     raise Exception('Could not open {}'.format(self.serial.port))

    def close(self): # type: () -> None
        """
        If the serial port is open, it closes it.
        """
        if self.serial.is_open:
            self.serial.close()
        # self.setRTS(False) # set DTR to 0V

    def write(self, pkt):
        pkts = bytearray(pkt)
        bpkts = bytes(pkts)
        self.serial.write(bpkts)
        sleep(0.001)

    def read(self):
        num = self.serial.in_waiting
        if num > 0:
            data = self.serial.read(num)
            # for d in data:
            #     print(int(d), end=',')
            # print(" ")
            return list(bytearray(data))
            # dd = servo.decodePacket(d)
            # for d in dd:
            #     print(servo.status_packet(d))
        # else:
        #     print(f"{Fore.RED}Oops ... {Fore.RESET}")
        return None

class ServoSerial:
    """
    A wrapper around pyserial to work with Dynamixel servos' half duplex
    interface. This requires extra hardware added to your normal full duplex
    serial port. Also, this uses the  RTS pin to toggle between Tx and Rx.

    All data that goes into this class via write() or returns from it via read()
    is a simple array of bytes (e.g., [1,34,234,1,0,24,67]). Internally, the class
    transforms those into a binary stream.

    This class also uses Packet to find and verify what is returned form read()
    is a valid packet.

    RPi3 sucks ... they screwed up the serial port, the RTS pin doesn't work so I
    just toggle pin 17 and treat it as an output pin.
    """
    # my board: DTR=True(3.3V), DTR=False(0V)
    DD_WRITE = False      # data direction set to write .. RTS is backwards
    DD_READ = not DD_WRITE        # data direction set to read .. RTS is backwards
    # old way, did I screw soemthing up?
    # DD_WRITE = True      # data direction set to write
    # DD_READ = not DD_WRITE        # data direction set to read

    # SLEEP_TIME = 0.0    # sleep time between read/write
    # SLEEP_TIME = 0.005    # sleep time between read/write
    # SLEEP_TIME = 0.0005    # sleep time between read/write
    # SLEEP_TIME = 0.00005    # sleep time between read/write
    # fake = False
    loop_addr = 'loop://'
    # pi_pin: = None

    def __init__(self, port, baud_rate=1000000): # type: (str,int) -> None
        """
        Constructor: sets up the serial port

        If you want to use a USB serial port, then set rts_hw to 0 (False). If you
        want to use the RPi seiral port, then you need to use a pin to toggle TX/Rx.
        Set rst_hw to any valid BCM pin greater than 0.
        """
        if port in ['dummy', 'fake', 'test', '/dev/null']:
            self.serial = PySerial.serial_for_url(self.loop_addr, timeout=0.1)
        else:
            self.serial = PySerial.Serial()
            self.serial.baudrate = baud_rate
            self.serial.port = port
        # print(self.serial)

        # minimum status packet is 6 bytes or 6*8 bits
        # the default time delay on the servo is 0.5 msec before it returns a status pkt
        # self.serial.timeout = 0.0001  # time out waiting for blocking read()
        # self.serial.timeout = 0.005 # works kjw
        self.serial.timeout = 6*8/baud_rate + 0.0005
        self.datarate = baud_rate

    def __del__(self) -> None:
        """
        Destructor: closes the serial port
        """
        self.close()

    def setRTS(self, level: bool) -> None:
        # time.sleep(self.SLEEP_TIME)
        # only need one of these, but the lazy option to if statements to determine
        # if using DTR or RTS as the direction pin
        # normal for my boards
        self.serial.dtr = level
        self.serial.rts = level

        # diff
        # self.serial.dtr = not level
        # self.serial.rts = not level

    def open(self) -> None:
        if self.serial.is_open:
            return True

        self.serial.open()

        self.setRTS(self.DD_WRITE)
        if self.serial.isOpen():
            # print('Opened {} @ {}'.format(self.serial.name, self.serial.baudrate))
            # print(self.serial.get_settings())
            return True

        return False
            # raise Exception('Could not open {}'.format(self.serial.port))

    @staticmethod
    def decode(buff: Sequence[int]) -> List[int]:
        """
        Transforms the raw buffer data read in into a list of bytes

        does serial.to_bytes() do the same thing?
        """
        pp = list(bytearray(buff))
        if 0 == len(pp) == 1:
            pp = []
        return pp

    # def read(self, how_much: int=128) -> Union[List[int], None]:  # FIXME: 128 might be too much ... what is largest?
    def read(self, how_much=None):
        """
        This toggles the RTS pin and reads in data. It also converts the buffer
        back into a list of bytes and searches through the list to find valid
        packets of info. If there is more than one packet, this returns an
        array of valid packets.
        """
        # self.setRTS(self.DD_READ)
        # time.sleep(0.001)
        if how_much is None:
            how_much = self.serial.in_waiting
        if how_much == 0:
            return None

        data = self.serial.read(how_much)
        # print('read() data', data, 'len(data)', len(data))
        if data:
            # print('>> read:', data)
            data = self.decode(data)
            # print('decode', data)
            # ret = Packet.findPkt(data)
            # print('ret', ret)
        else:
            # data = []
            data = None
        return data

    def write(self, pkt: List[int]) -> int:
        """
        This is a simple serial write command. It toggles the RTS pin and formats
        all of the data into bytes before it writes.

        in:
            pkt - array of bytes to send: [2,3,4]
        return:
            number of bytes written to serial port
        """
        # print('>> write:', pkt)
        self.setRTS(self.DD_WRITE)
        self.serial.reset_input_buffer() # can cause problems
        # prep data array for transmition
        pkts = bytearray(pkt)
        bpkts = bytes(pkts)

        num = self.serial.write(bpkts)
        time.sleep(8*len(pkt)/self.datarate) # transmit time

        # want to allow the servos max time to respond, if write line held too
        # long, then you will NOT get a response
        self.setRTS(self.DD_READ)
        # time.sleep(8*len(pkt)/self.datarate) # transmit time

        return num

    # def sendPkt(self, pkt: List[int], retry: int=5, sleep_time: float=0.01) -> Union[List[int], None]:
    def sendPkt(self, pkt, retry=5, sleep_time=0.01): # (Sequence[int], int, float)-> Union[List[int], None]
        """
        Sends a packet and waits for a return. If no return is given, then it
        resends the packet. If an error occurs, it also resends the packet.

        in:
            pkt - command packet to send to servo
            retry - how many retries should this do? default = 5
        return:
            None or response packet
        """

        ID = pkt[2]

        ans = None
        # while retry:
        for _ in range(retry):
            self.write(pkt)  # send packet to servo
            time.sleep(sleep_time)  # need to wait some time between read/write, max time is 508 usec for servo
            ans = self.read()  # get return status packet

            if ans and len(ans) > 6:
                ret_id = ans[2]
                if ID == ret_id:
                    # print(Fore.GREEN + f">> {ID} == {ret_id}" + Fore.RESET)
                    break
                else:
                    print(Fore.RED + f"** Packet has invalid ID, expect: {ID} got: {ret_id}" + Fore.RESET)
            # else:
            #     print(Fore.RED + f">> no packet" + Fore.RESET)

            time.sleep(sleep_time)
            # retry -= 1

        return ans

    def close(self): # type: () -> None
        """
        If the serial port is open, it closes it.
        """
        if self.serial.is_open:
            self.serial.close()
        self.setRTS(False) # set DTR to 0V

    # def flushInput(self):
    #     """
    #     Flush the input.
    #     """
    #     self.serial.flushInput()
