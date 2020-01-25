from servo_serial import ServoSerial
try:
    import RPi.GPIO as GPIO
except ImportError as e:
    print(f"*** {e} ***")
    raise


class PiServoSerial(ServoSerial):
    def __init__(self, port, pin, baud_rate=1000000):
        super.__init__(port, baud_rate)
        self.pi_pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

    def __del__(self):
        """
        Destructor: closes the serial port
        """
        self.close()
        GPIO.cleanup()

    def setRTS(self, level):
        time.sleep(self.SLEEP_TIME)
        GPIO.output(self.pi_pin, not level)
