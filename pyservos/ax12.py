from pyservos.protocol1 import Protocol1
from enum import IntFlag

P1Errors = IntFlag('P1Errors',
    {
        'voltage':     2**0, # voltage is outside operating range
        'angle':       2**1, # invalid angle
        'overheat':    2**2, # temperature is out of range
        'range':       2**3, # instruction is out of range
        'checksum':    2**4, # invalid checksum
        'overload':    2**5, # current can't meet required torque
        'instruction': 2**6, # invalid instruction
        'none':        2**7  # not used
    }
)


class AX12(Protocol1):
    # registers
    """
    This class handles the AX-12A servo using Dynimel's Protocol version 1.0.
    """
    # SERVO_ID = 1  # used to tell AX and XL servos appart
    # SERVO_TYPE = ServoTypes.ax12
    MAX_RPM = int(59/0.111)
    MAX_ANGLE = 300
    NAME = "AX-12A"

    # # --------- INSTRUCTIONS -----
    # PING      = 0x01
    # READ      = 0x02
    # WRITE     = 0x03
    # REG_WRITE = 0x04
    # ACTION    = 0x05
    # RESET     = 0x06 # reset to factory levels: 1,2,3
    # REBOOT    = 0x08
    # SYNC_WRITE = 0x83
    # BULK_READ  = 0x92

    # -------- EEPROM -------------
    MODEL_NUMBER    = 0
    VER_FIRMWARE    = 2
    ID              = 3
    BAUD_RATE       = 4
    DELAY_TIME      = 5
    CW_ANGLE_LIMIT  = 6   # min angle, default 0
    CCW_ANGLE_LIMIT = 8   # max angle, default 300
    CONTROL_MODE    = 11  # joint or wheel mode, default joint (servo)
    MAX_TORQUE      = 15
    RETURN_LEVEL    = 17

    # -------- RAM ----------------
    TORQUE_ENABLE    = 24  # servo mode on/off - turn into wheel
    LED              = 25
    GOAL_POSITION    = 30
    GOAL_VELOCITY    = 32
    GOAL_TORQUE      = 34
    PRESENT_POSITION = 36  # current servo angle
    PRESENT_SPEED    = 38  # current speed
    PESENT_LOAD      = 40  # current load
    PESENT_VOLTAGE   = 42  # current voltage
    PESENT_TEMP      = 43  # current temperature
    MOVING           = 46
    PUNCH            = 48
    HW_ERROR_STATUS  = 50
    PUNCH            = 51

    # --------- OTHER -------------
    RESET_ALL                  = 0xFF
    RESET_ALL_BUT_ID           = 0x01
    RESET_ALL_BUT_ID_BAUD_RATE = 0x02
    LED_ON                     = 1
    LED_OFF                    = 0
    BROADCAST_ADDR             = 0xfe  # a packet with this ID will go to all servos
    WHEEL_MODE                 = 1
    JOINT_MODE                 = 2  # normal servo
    DR_1000000                 = 1  # bps = 2000000/(data + 1)
    DR_500000                  = 2
    DR_400000                  = 4
    DR_250000                  = 7
    DR_200000                  = 9
    DR_115200                  = 16
    DR_57600                   = 34
