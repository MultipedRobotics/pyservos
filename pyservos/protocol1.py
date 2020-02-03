from enum import IntFlag
from pyservos.utils import angle2int, le
from pyservos.common import ResetLevels
# from typing import Sequence, List, Union


class Protocol1:
    """
    This is a wrapper class for the ax-12 servos. It can only talk
    to one servo type at a time.

    Note: this class cannot be used by itself, since it references parameters
    that are not part of the class. The child class will set the value of
    these registers (i.e., self.WRITE, self.READ)
    """

    # --------- INSTRUCTIONS -----
    PING      = 0x01
    READ      = 0x02
    WRITE     = 0x03
    REG_WRITE = 0x04
    ACTION    = 0x05
    RESET     = 0x06 # reset to factory levels: 1,2,3
    REBOOT    = 0x08
    SYNC_WRITE = 0x83
    BULK_READ  = 0x92

    def makePingPacket(self, ID=None):
        """
        Pings a servo
        """
        if not ID:
            ID = self.BROADCAST_ADDR
        pkt = self.makePacket(ID, self.PING)
        return pkt

    def makeWritePacket(self, ID, reg, values=None):
        """
        Creates a packet that writes a value(s) to servo ID at location reg. Make
        sure the values are in little endian (use Packet.le() if necessary) for 16 b
        (word size) values.
        """
        if values:
            params = [reg] + values
        else:
            params = [reg]

        pkt = self.makePacket(ID, self.WRITE, params)
        return pkt

    def makeReadPacket(self, ID, reg, values=None):
        """
        Creates a packet that reads the register(s) of servo ID at location reg. Make
        sure the values are in little endian (use Packet.le() if necessary) for 16 b
        (word size) values.
        """
        if values:
            params = [reg] + values
        else:
            params = [reg]
        pkt = self.makePacket(ID, self.READ, params)
        return pkt

    def makeResetPacket(self, ID, level=3):
        """
        Resets a servo.
        1 - all
        2 - all but ID
        3 - all but ID and baudrate (default)
        """
        if ResetLevel.all == level:
            lvl = self.RESET_ALL
        elif ResetLevel.allButID == level:
            lvl = self.RESET_ALL_BUT_ID
        else:  # set as default since it is the safest if things go bad
            lvl = self.RESET_ALL_BUT_ID_BAUD_RATE

        # pkt = self.makePacket(ID, self.RESET, [lvl])
        ptk = None
        return pkt

    def makeRebootPacket(self, ID):
        """
        Reboots a servo
        """

        pkt = self.makePacket(ID, self.REBOOT)
        return pkt

    def makeSetIDPacket(self, id, new_id):
        pkt = self.makeWritePacket(id, self.ID, [new_id])
        return pkt

    # def makeGetAngle(self, ID):
    #     pkt = self.makeReadPacket(ID, )

    def makeServoMovePacket(self, ID, angle, degrees=True):
        """
        Commands the servo to an angle (0-300 deg) or radians (0-5.24 rads)
        angle: [0-300] deg or [0.0-5.24] rads
        degrees: True (default) or False
        """
        val = angle2int(angle, degrees)
        pkt = self.makeWritePacket(ID, self.GOAL_POSITION, val)

        return pkt

    def makeServoMoveCountsPacket(self, ID, angle):
        """
        Commands the servo to an angle in counts (0-1023)
        """
        val = le(int(angle))
        pkt = self.makeWritePacket(ID, self.GOAL_POSITION, val)

        return pkt

    def makeSyncMovePacket(self, info, degrees=True):
        """
        Write sync angle information to servos.

        info = [[ID, angle], [ID, angle], ...]
        ID: servo ID
        angle: 0-300 degrees or in radians
        """
        data = []

        # since all servo angles have the same register addr (GOAL_POSITION)
        # and data size (2), a sinc packet is smart choice
        # compare bulk vs sync for the same commands:
        # bulk = 94 bytes
        # sync = 50 bytes
        for cmd in info:
            data.append(cmd[0])  # ID
            angle = angle2int(cmd[1], degrees)
            data.append(angle[0])  # LSB
            data.append(angle[1])  # MSB

        pkt = self.makeSyncWritePacket(self.GOAL_POSITION, data)
        return pkt

    def makeSyncMoveSpeedPacket(self, info, degrees=True):
        """
        Write sync angle information to servos.

        info = [[ID, angle, speed], [ID, angle, speed], ...]
        ID: servo ID
        angle: 0-300 degrees or in radians
        speed: 0-1023
        """
        data = []
        for cmd in info:
            data.append(cmd[0])  # ID
            angle = angle2int(cmd[1], degrees)
            data.append(angle[0])  # LSB
            data.append(angle[1])  # MSB
            speed = le(cmd[2])
            data.append(speed[0])  # LSB
            data.append(speed[1])  # MSB

        pkt = self.makeSyncWritePacket(self.GOAL_POSITION, data)
        return pkt

    def makeSyncWritePacket(self, reg, info):
        """
        Write sync angle information to servos.
        Status Packet will not be returned because Broadcast ID(0xFE) is used

        info = [[ID, data1, ...], [ID, data1, ...], ...]
        """
        data = []
        data.append(reg)  # addr
        data.append(len(info[0])-1)  # data length not counting ID
        for cmd in info:
            data += cmd

        ID = self.BROADCAST_ADDR
        instr = self.SYNC_WRITE
        pkt = self.makePacket(ID, instr, data)  # create packet
        return pkt

    def makeBulkReadPacket(self, data):
        """
        data = [[data len, ID, addr], [data len, ID, addr], ...]
        """
        ID = self.BROADCAST_ADDR
        instr = self.BULK_READ
        dd = []
        for d in data:
            dd += d
        pkt = self.makePacket(ID, instr, dd)  # create packet
        return pkt

    def makeLEDPacket(self, ID, value):
        """
        Turn on/off the servo LED and also sets the color.
        """
        if value < 0 or value > 1:
            raise Exception("ERROR: LED can only be off or on: {}".format(value))
            # value = [value]
        # elif self.SERVO_ID == XL320.SERVO_ID:
        #     # print('Not implemented yet')
        #     value = [0, value]

        pkt = self.makeWritePacket(ID, self.LED, [value])
        return pkt

    def makeSpeedPacket(self, speed):
        """
        Set max speed for all servos
        speed - [0-1023] in units of 0.111 rpm. If speed = 0, then max motor
                speed is used. You cannot exceed max servo speed.
        """
        speed = speed if (speed <= self.MAX_RPM) else self.MAX_RPM
        pkt = self.makeWritePacket(
            self.BROADCAST_ADDR,
            self.GOAL_VELOCITY,
            le(speed)
        )
        return pkt

    def makeServoInfoPacket(self, ID):
        pkt = self.makeReadPacket(ID, self.MODEL_NUMBER, [5])
        return pkt

    # makeReadPacket(self, ID, reg, values=None)
    def makeReadAnglePacket(self, ID):
        return self.makeReadPacket(ID, self.PRESENT_POSITION, [2])

    def decodePacket(self, pkts):
        return self.find_packets(pkts)

    def processStatusPacket(self, pkt):
        return self.status_packet(pkt)

    @staticmethod
    def check_sum(data):
        """
        checksum = 255 - ((id + length + data1 + data2 + ... + dataN) & 255)
        """
        # print(data)
        return 255 - (sum(data) & 255)

    def makePacket(self, ID, instr, params=None):
        """
        This makes a generic packet.

        0xFF, 0xFF, ID, LENGTH, INST, PARAM 1, PARAM 2, ..., PARAM N, CHECKSUM]
        in:
            ID - servo id
            instr - instruction
            params - instruction parameter values
        out: packet
        """
        pkt = [0xff, 0xff, ID]
        if params:
            # print(params)
            length = len(params) + 2
            pkt += [length, instr]
            pkt += params
            # print(self.check_sum(pkt[2:]))
            pkt += [self.check_sum(pkt[2:])]
        else:
            pkt += [2, instr, self.check_sum([ID, 2, instr])]

        return pkt

    def find_packets(self, pkt):
        """
        Search through a string of binary for a valid ax-12 package.

        in: buffer to search through
        out: a list of valid data packet
        """
        # print('findpkt', pkt)
        # print('-----------------------')
        ret = []
        while len(pkt)-6 >= 0:
            try:
                # print(pkt)
                # check for header
                if pkt[0:2] != [0xFF, 0xFF]:
                    pkt.pop(0)  # get rid of the first index
                    continue
                length = pkt[3]  # get length
                crc_pos = 3 + length
                pkt_crc = pkt[crc_pos]  # packet crc
                crc = self.check_sum(pkt[2:crc_pos])  # calculated crc
                if pkt_crc == crc:
                    pkt_end = crc_pos+1
                    ret.append(pkt[:pkt_end])
                    del pkt[:pkt_end]
                else:
                    pkt.pop(0)
            except Exception:
                pkt.pop(0)
        return ret

    def status_packet(self, pkt):
        def getError(err):
            errors = [
                'Input Voltage',  # 0
                'Angle Limit',
                'Overheating',
                'Range',
                'Checksum',
                'Overload',
                'Instrunction',
                'None'  # 7
            ]
            # ret = None
            if not (err == 128 or err == 0):
                err_str = []
                for i in range(0, 8):
                    if (err >> i) & 1:
                        err_str.append(errors[i])
                ret = ','.join(err_str)
            else:
                ret = errors[7]
            return ret

        ret = {
            'id': pkt[2],
            'error str': getError(pkt[4]),
            'error num': pkt[4],
            'params': pkt[5:-1],
            'raw': list(pkt)
        }
        return ret
