from pyservos.protocol2 import Protocol2



class XL430(Protocol2):
    MAX_ANGLE = 360
    NAME = "XL-430"

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
    MODEL_INFO      = 2
    VER_FIRMWARE    = 6
    ID              = 7
    BAUD_RATE       = 8
    DELAY_TIME      = 9
    DRIVE_MODE      = 10   # min angle, default 0
    OPERATING_MODE  = 11   # max angle, default 300
    SECOND_ID       = 12  # joint or wheel mode, default joint (servo)
    PROTOCOL        = 13
    HOMING_OFFSET   = 20
    MOVING_THRESHOLD = 24
    TEMP_LIMIT      = 31
    MAX_VOLT_LIMIT  = 32
    MIN_VOLT_LIMIT  = 34
    PWM_LIMIT       = 36
    VELOCITY_LIMIT  = 44
    MAX_POS_LIMIT   = 48
    MIN_POS_LIMIT   = 52
    SHUTDOWN        = 63

    # -------- RAM ----------------
    TORQUE_ENABLE    = 64  # servo mode on/off - turn into wheel
    LED              = 65
    # GOAL_POSITION    = 30
    # GOAL_VELOCITY    = 32
    # GOAL_TORQUE      = 35
    # PRESENT_POSITION = 37  # current servo angle
    # PRESENT_SPEED    = 39  # current speed
    # PESENT_LOAD      = 41  # current load
    # PESENT_VOLTAGE   = 45  # current voltage
    # PESENT_TEMP      = 46  # current temperature
    # MOVING           = 49
    # HW_ERROR_STATUS  = 50
    # PUNCH            = 51
