from pyservos.protocol2 import Protocol2
from pyservos.common import ResetLevels

class XL320(Protocol2):
    # SERVO_ID = 2  # used to tell AX and XL servos appart
    # SERVO_TYPE = ServoTypes.xl320
    MAX_ANGLE = 300
    NAME = "XL-320"

    # # --------- INSTRUCTIONS -----
    # PING      = 0x01
    # READ      = 0x02
    # WRITE     = 0x03
    # REG_WRITE = 0x04
    # ACTION    = 0x05
    # RESET     = 0x06
    # REBOOT    = 0x08
    # STATUS    = 0x55
    # SYNC_READ  = 0x82
    # SYNC_WRITE = 0x83
    # BULK_READ  = 0x92
    # BULK_WRITE = 0x93

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
    GOAL_TORQUE      = 35
    PRESENT_POSITION = 37  # current servo angle
    PRESENT_SPEED    = 39  # current speed
    PESENT_LOAD      = 41  # current load
    PESENT_VOLTAGE   = 45  # current voltage
    PESENT_TEMP      = 46  # current temperature
    MOVING           = 49
    HW_ERROR_STATUS  = 50
    PUNCH            = 51

    # --------- OTHER -------------
    RESET_ALL                  = 0xFF
    RESET_ALL_BUT_ID           = 0x01
    RESET_ALL_BUT_ID_BAUD_RATE = 0x02
    LED_WHITE                  = 7
    LED_BLUE_GREEN             = 6
    LED_PINK                   = 5
    LED_BLUE                   = 4
    LED_YELLOW                 = 3
    LED_GREEN                  = 2
    LED_RED                    = 1
    LED_OFF                    = 0
    BROADCAST_ADDR             = 0xfe  # a packet with this ID will go to all servos
    WHEEL_MODE                 = 1
    JOINT_MODE                 = 2  # normal servo
    DR_9600                    = 0  # 0: 9600, 1:57600, 2:115200, 3:1Mbps
    DR_57600                   = 1
    DR_115200                  = 2
    DR_1000000                 = 3
