from enum import IntFlag
from pyservos.utils import angle2int, le
from pyservos.common import ResetLevels

# ResetLevels = IntFlag('ResetLevels', 'all allButID allButIDDR')

crc_table = [
    0x0000, 0x8005, 0x800F, 0x000A, 0x801B, 0x001E, 0x0014, 0x8011,
    0x8033, 0x0036, 0x003C, 0x8039, 0x0028, 0x802D, 0x8027, 0x0022,
    0x8063, 0x0066, 0x006C, 0x8069, 0x0078, 0x807D, 0x8077, 0x0072,
    0x0050, 0x8055, 0x805F, 0x005A, 0x804B, 0x004E, 0x0044, 0x8041,
    0x80C3, 0x00C6, 0x00CC, 0x80C9, 0x00D8, 0x80DD, 0x80D7, 0x00D2,
    0x00F0, 0x80F5, 0x80FF, 0x00FA, 0x80EB, 0x00EE, 0x00E4, 0x80E1,
    0x00A0, 0x80A5, 0x80AF, 0x00AA, 0x80BB, 0x00BE, 0x00B4, 0x80B1,
    0x8093, 0x0096, 0x009C, 0x8099, 0x0088, 0x808D, 0x8087, 0x0082,
    0x8183, 0x0186, 0x018C, 0x8189, 0x0198, 0x819D, 0x8197, 0x0192,
    0x01B0, 0x81B5, 0x81BF, 0x01BA, 0x81AB, 0x01AE, 0x01A4, 0x81A1,
    0x01E0, 0x81E5, 0x81EF, 0x01EA, 0x81FB, 0x01FE, 0x01F4, 0x81F1,
    0x81D3, 0x01D6, 0x01DC, 0x81D9, 0x01C8, 0x81CD, 0x81C7, 0x01C2,
    0x0140, 0x8145, 0x814F, 0x014A, 0x815B, 0x015E, 0x0154, 0x8151,
    0x8173, 0x0176, 0x017C, 0x8179, 0x0168, 0x816D, 0x8167, 0x0162,
    0x8123, 0x0126, 0x012C, 0x8129, 0x0138, 0x813D, 0x8137, 0x0132,
    0x0110, 0x8115, 0x811F, 0x011A, 0x810B, 0x010E, 0x0104, 0x8101,
    0x8303, 0x0306, 0x030C, 0x8309, 0x0318, 0x831D, 0x8317, 0x0312,
    0x0330, 0x8335, 0x833F, 0x033A, 0x832B, 0x032E, 0x0324, 0x8321,
    0x0360, 0x8365, 0x836F, 0x036A, 0x837B, 0x037E, 0x0374, 0x8371,
    0x8353, 0x0356, 0x035C, 0x8359, 0x0348, 0x834D, 0x8347, 0x0342,
    0x03C0, 0x83C5, 0x83CF, 0x03CA, 0x83DB, 0x03DE, 0x03D4, 0x83D1,
    0x83F3, 0x03F6, 0x03FC, 0x83F9, 0x03E8, 0x83ED, 0x83E7, 0x03E2,
    0x83A3, 0x03A6, 0x03AC, 0x83A9, 0x03B8, 0x83BD, 0x83B7, 0x03B2,
    0x0390, 0x8395, 0x839F, 0x039A, 0x838B, 0x038E, 0x0384, 0x8381,
    0x0280, 0x8285, 0x828F, 0x028A, 0x829B, 0x029E, 0x0294, 0x8291,
    0x82B3, 0x02B6, 0x02BC, 0x82B9, 0x02A8, 0x82AD, 0x82A7, 0x02A2,
    0x82E3, 0x02E6, 0x02EC, 0x82E9, 0x02F8, 0x82FD, 0x82F7, 0x02F2,
    0x02D0, 0x82D5, 0x82DF, 0x02DA, 0x82CB, 0x02CE, 0x02C4, 0x82C1,
    0x8243, 0x0246, 0x024C, 0x8249, 0x0258, 0x825D, 0x8257, 0x0252,
    0x0270, 0x8275, 0x827F, 0x027A, 0x826B, 0x026E, 0x0264, 0x8261,
    0x0220, 0x8225, 0x822F, 0x022A, 0x823B, 0x023E, 0x0234, 0x8231,
    0x8213, 0x0216, 0x021C, 0x8219, 0x0208, 0x820D, 0x8207, 0x0202
]

class Protocol2:
    """
    This is a wrapper class for the xl-320 and ax-12 servos. It can only talk
    to one servo type at a time.
    """

    # --------- INSTRUCTIONS -----
    PING      = 0x01
    READ      = 0x02
    WRITE     = 0x03
    REG_WRITE = 0x04
    ACTION    = 0x05
    RESET     = 0x06
    REBOOT    = 0x08
    CLEAR     = 0X10
    STATUS    = 0x55
    SYNC_READ  = 0x82
    SYNC_WRITE = 0x83
    BULK_READ  = 0x92
    BULK_WRITE = 0x93

    # def __init__(self, kind):
    #     self.base = kind()

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
            params = le(reg) + values
        else:
            params = le(reg)

        pkt = self.makePacket(ID, self.WRITE, params)
        return pkt

    def makeReadPacket(self, ID, reg, values=None):
        """
        Creates a packet that reads the register(s) of servo ID at location reg. Make
        sure the values are in little endian (use Packet.le() if necessary) for 16 b
        (word size) values.
        """
        pkt = self.makePacket(ID, self.READ, [reg, values])
        return pkt

    # def makeResetPacket(self, ID, level=0):
    #     """
    #     Resets a servo.
    #     """
    #     params = [XL320.RESET_ALL_BUT_ID]
    #     pkt = self.makePacket(ID, self.RESET, params)
    #     return pkt

    def makeResetPacket(self, ID, level):
        """
        Resets a servo.
        """
        if ResetLevels.all == level:
            params = [self.RESET_ALL]
        elif ResetLevels.allButID == level:
            params = [self.RESET_ALL_BUT_ID]
        elif ResetLevels.allButIDDR == level:
            params = [self.RESET_ALL_BUT_ID_BAUD_RATE]
        else:
            raise Exception("Invalid reset level")

        pkt = self.makePacket(ID, self.RESET, params)
        return pkt

    def makeRebootPacket(self, ID):
        """
        Reboots a servo
        """

        pkt = self.makePacket(ID, self.REBOOT)
        return pkt

    def makeServoMovePacket(self, ID, angle, degrees=True):
        """
        Commands the servo to an angle (in degrees)
        """
        # if degrees and not (0.0 <= angle <= 300.0):
        #     raise Exception('makeServoMovePacket(), angle [deg] out of bounds: {}'.format(angle))
        # elif (not degrees) and (not (0.0 <= angle <= 5.23598776)):
        #     raise Exception('makeServoMovePacket(), angle [rads] out of bounds: {}'.format(angle))
        # val = int(angle/300*1023)
        val = angle2int(angle, degrees)
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
        pkt = self.makePacket(ID, instr, data)  # create packet
        return pkt

    def makeLEDPacket(self, ID, value):
        """
        Turn on/off the servo LED and also sets the color.
        """
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

    def decodePacket(self, pkts):
        return self.find_packets(pkts)

    def processStatusPacket(self, pkt):
        return self.status_packet(pkt)

    def check_sum(self, data_blk):
        """
        Calculate crc

        in: data_blk - entire packet except last 2 crc bytes
        out: crc_accum - 16 word
        """
        data_blk_size = len(data_blk)
        crc_accum = 0
        for j in range(data_blk_size):
            i = ((crc_accum >> 8) ^ data_blk[j]) & 0xFF
            crc_accum = ((crc_accum << 8) ^ crc_table[i])
            crc_accum &= 0xffff  # keep to 16 bits

        return crc_accum

    def makePacket(self, ID, instr, params=None):
        """
        This makes a generic packet.

        TODO: look a struct ... does that add value using it?

        0xFF, 0xFF, 0xFD, 0x00, ID, LEN_L, LEN_H, INST, PARAM 1, PARAM 2, ..., PARAM N, CRC_L, CRC_H]
        in:
            ID - servo id
            instr - instruction
            params - [register, instruction parameter values]
        out: packet
        """
        pkt = []
        # [header, reserved, 0x00, ID, len low, len high, instruction]
        pkt += [0xFF, 0xFF, 0xFD, 0x00, ID, 0x00, 0x00, instr]  # header
        # pkt += [0x00]  # reserved byte
        # pkt += [ID]
        # pkt += [0x00, 0x00]  # length placeholder
        # pkt += [instr]  # instruction
        # if reg:
        #     pkt += le(reg)  # not everything has a register
        if params:
            pkt += params    # not everything has parameters

        length = le(len(pkt) - 5)  # length = len(packet) - (header(3), reserve(1), id(1))
        pkt[5] = length[0]  # L
        pkt[6] = length[1]  # H

        crc = self.check_sum(pkt)
        pkt += le(crc)

        return pkt

    def find_packets(self, pkt):
        """
        Search through a string of binary for a valid xl320 package.

        in: buffer to search through
        out: a list of valid data packet
        """
        # print('findpkt', pkt)
        # print('-----------------------')
        ret = []
        while len(pkt)-10 >= 0:
            if pkt[0:4] != [0xFF, 0xFF, 0xFD, 0x00]:
                pkt.pop(0)  # get rid of the first index
                # print(' - pop:', pkt)
                continue
            # print(' > good packet')
            length = (pkt[6] << 8) + pkt[5]
            # print(' > length', length)
            crc_pos = 5 + length
            pkt_crc = pkt[crc_pos:crc_pos + 2]
            crc = le(self.check_sum(pkt[:crc_pos]))
            # if len(pkt) < (crc_pos + 1):
            #     print('<<< need more data for findPkt >>>')

            # print(' > calc crc', crc)
            # print(' > pkt crc', pkt_crc)
            if pkt_crc == crc:
                pkt_end = crc_pos+2
                ret.append(pkt[:pkt_end])
                # print(' > found:', pkt[:pkt_end])
                # print(' > pkt size', pkt_end)
                del pkt[:pkt_end]
                # print(' > remaining:', pkt)
            else:
                pkt_end = crc_pos+2
                # print(' - crap:', pkt[:pkt_end])
                del pkt[:pkt_end]
        # print('findpkt ret:', ret)
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
            ret = None
            if err != 128:
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
