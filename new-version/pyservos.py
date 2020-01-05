from __future__ import print_function

class Protocol1(object):
    protocol = 1
    def make_packet(self, ID, data):
        pass
    def make_write_packet(self, ID, reg, data):
        pass
    def make_read_packet(self, ID, reg, data):
        pass
    def make_sync_read_packet(self, reg, data):
        pass
    def make_sync_write_packet(self, reg, data):
        pass
    def crc(self, pkt):
        pass
    def decodePacket(self, pkt):
        # find packet
        # for each packet found, decode
        pass

class Protocol2(object):
    protocol = 2
    def make_packet(self, ID, data):
        pass
    def make_write_packet(self, ID, reg, data):
        pass
    def make_read_packet(self, ID, reg, data):
        pass
    def make_sync_read_packet(self, reg, data):
        pass
    def make_sync_write_packet(self, reg, data):
        pass
    def crc(self, pkt):
        pass
    def decodePacket(self, pkt):
        pass

class AX12(object):
    name = 'AX12A'
    # registers
    def __init__(self):
        self.proto = Protocol1()
    def make_led_packet(self, ID, value):
        pass

class XL320(object):
    name = 'XL320'
    # registers
    def __init__(self):
        self.proto = Protocol2()
    def make_led_packet(self, ID, value):
        pass

class XL430(object):
    name = 'XL430'
    # registers
    def __init__(self):
        self.proto = Protocol2()
    def make_led_packet(self, ID, value):
        pass

class Packet(object):
    """
    This is a generic interface (wrapper) around 2 different Robotis protocols.
    It creates packets by passing info to the correct protocol function. You could
    skip this layer and talke directly to the protocol layer, but, most of the
    advanced functions live here.
    """
    def __init__(self, servo):
        self.servo = servo()
        self.proto = servo.proto
        self.protocol = servo.proto.protocol

    def makePacket(self, ID, reg, values=None):
        return self.proto.make_packet(ID, reg, values)

    def makePingPacket(self, ID=None):
        pass

    def makeReadPacket(self, ID, reg, values=None):
        return self.proto.make_read_packet(ID, reg, values)

    def makeWritePacket(self, ID, reg, values=None):
        return self.proto.make_write_packet(ID, reg, values)

    def makeResetPacket(self, ID, level=0):
        pass

    def makeRebootPacket(self, ID, level=0):
        if self.protocol == 1:
            print()
            return None
        pass

    def makeLEDPacket(self, ID, value):
        return = self.servo.make_led_packet(ID, value)

class ServoPacket(Packet):
    def __init__(self, servo):
        Packet.__init__(self, servo)

    def makeAnglePacket(self, ID, angle, degrees=True):
        pass

    def makeSyncAnglePacket():
        pass

    def makeServoModePacket(self, ID):
        pass

class WheelPacket(Packet):
    def __init__(self, servo):
        Packet.__init__(self, servo)

    def makeVelocityPacket(self, ID, speed):
        pass

    def makeWheelModePacket(self, ID):
        pass

    def makeEncoderPacket(self, ID):
        pass
