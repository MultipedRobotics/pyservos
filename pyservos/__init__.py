try:
    from enum import IntFlag
except ImportError:
    from enum import IntEnum as IntFlag

servoTypes = {
    1: 'AX-12A',
    2: 'XL-320',
    3: 'XL-430'
}

ServoTypes = IntFlag('ServoTypes', 'ax12 xl320 xl430')

ErrorsXL320 = IntFlag('ErrorsXL320',
    'inputVoltage angleLimit \
    overheating range checksum \
    overload instrunction none')


# from pyservos.servoserial import ServoSerial
from pyservos.packet import Packet
from pyservos.ax12 import AX12
from pyservos.xl320 import XL320
from pyservos.packet import Packet

__copyright__ = 'Copyright (c) 2016 Kevin Walchko'
__license__ = 'MIT'
__author__ = 'Kevin J. Walchko'
__version__ = '1.0.3'
