# from typing import List, Sequence
from .servo_serial import ServoSerial # type: ignore
import time

try:
    import RPi.GPIO as GPIO # type: ignore
except ImportError as e:
    print(f"*** {e} ***")
    raise


class PiServoSerial(ServoSerial):
    def __init__(self, port, pin, baud_rate=1000000): # type: (str,int,int) -> None
        super.__init__(port, baud_rate) # type: ignore
        self.pi_pin = pin # type: int
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

    def __del__(self): # type: () -> None
        """
        Destructor: closes the serial port
        """
        self.close()
        GPIO.cleanup()

    def setRTS(self, level): # type: (int) -> None
        time.sleep(self.SLEEP_TIME)
        GPIO.output(self.pi_pin, not level)
