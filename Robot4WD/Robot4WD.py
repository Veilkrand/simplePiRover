import time
import atexit

from Adafruit_MotorHAT import Adafruit_MotorHAT


class Robot4WD(object):

    #handling states
    STOP=0
    MOVING_FORWARD=1
    MOVING_BACKWARD=2
    MOVING_LEFT=3
    MOVING_RIGHT=4
    moving_state=STOP

    def __init__(self, addr=0x60, left_id1=1, right_id1=2,left_id2=3, right_id2=4, left_trim=0, right_trim=0,
                 stop_at_exit=True):
        """Create an instance of the robot.  Can specify the following optional
        parameters:
         - addr: The I2C address of the motor HAT, default is 0x60.
         - left_id: The ID of the left motor, default is 1.
         - right_id: The ID of the right motor, default is 2.
         - left_trim: Amount to offset the speed of the left motor, can be positive
                      or negative and use useful for matching the speed of both
                      motors.  Default is 0.
         - right_trim: Amount to offset the speed of the right motor (see above).
         - stop_at_exit: Boolean to indicate if the motors should stop on program
                         exit.  Default is True (highly recommended to keep this
                         value to prevent damage to the bot on program crash!).
        """
        # Initialize motor HAT and left, right motor.
        self._mh = Adafruit_MotorHAT(addr)
        self._left1 = self._mh.getMotor(left_id1)
        self._left2 = self._mh.getMotor(left_id2)
        self._right1 = self._mh.getMotor(right_id1)
        self._right2 = self._mh.getMotor(right_id2)
        self._left_trim = left_trim
        self._right_trim = right_trim
        # Start with motors turned off.
        self._left1.run(Adafruit_MotorHAT.RELEASE)
        self._left2.run(Adafruit_MotorHAT.RELEASE)
        self._right1.run(Adafruit_MotorHAT.RELEASE)
        self._right2.run(Adafruit_MotorHAT.RELEASE)
        # Configure all motors to stop at program exit if desired.
        if stop_at_exit:
            atexit.register(self.stop)

    def _left_speed(self, speed):
        """Set the speed of the left motor, taking into account its trim offset.
        """
        assert 0 <= speed <= 255, 'Speed must be a value between 0 to 255 inclusive!'
        speed += self._left_trim
        speed = max(0, min(255, speed))  # Constrain speed to 0-255 after trimming.
        self._left1.setSpeed(speed)
        self._left2.setSpeed(speed)

    def _right_speed(self, speed):
        """Set the speed of the right motor, taking into account its trim offset.
        """
        assert 0 <= speed <= 255, 'Speed must be a value between 0 to 255 inclusive!'
        speed += self._right_trim
        speed = max(0, min(255, speed))  # Constrain speed to 0-255 after trimming.
        self._right1.setSpeed(speed)
        self._right2.setSpeed(speed)

    def stop(self):
        """Stop all movement."""

        if (self.moving_state==self.STOP):
            return

        self.moving_state=self.STOP

        self._left1.run(Adafruit_MotorHAT.RELEASE)
        self._left2.run(Adafruit_MotorHAT.RELEASE)
        self._right1.run(Adafruit_MotorHAT.RELEASE)
        self._right2.run(Adafruit_MotorHAT.RELEASE)

    def forward(self, speed, seconds=None):
        """Move forward at the specified speed (0-255).  Will start moving
        forward and return unless a seconds value is specified, in which
        case the robot will move forward for that amount of time and then stop.
        """

        if (self.moving_state==self.MOVING_FORWARD):
            return

        self.moving_state=self.MOVING_FORWARD

        # Set motor speed and move both forward.
        self._left_speed(speed)
        self._right_speed(speed)
        self._left1.run(Adafruit_MotorHAT.FORWARD)
        self._left2.run(Adafruit_MotorHAT.FORWARD)
        self._right1.run(Adafruit_MotorHAT.FORWARD)
        self._right2.run(Adafruit_MotorHAT.FORWARD)
        # If an amount of time is specified, move for that time and then stop.
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def backward(self, speed, seconds=None):
        """Move backward at the specified speed (0-255).  Will start moving
        backward and return unless a seconds value is specified, in which
        case the robot will move backward for that amount of time and then stop.
        """

        if (self.moving_state==self.MOVING_BACKWARD):
            return

        self.moving_state=self.MOVING_BACKWARD

        # Set motor speed and move both backward.
        self._left_speed(speed)
        self._right_speed(speed)
        self._left1.run(Adafruit_MotorHAT.BACKWARD)
        self._left2.run(Adafruit_MotorHAT.BACKWARD)
        self._right1.run(Adafruit_MotorHAT.BACKWARD)
        self._right2.run(Adafruit_MotorHAT.BACKWARD)
        # If an amount of time is specified, move for that time and then stop.
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def right(self, speed, seconds=None):
        """Spin to the right at the specified speed.  Will start spinning and
        return unless a seconds value is specified, in which case the robot will
        spin for that amount of time and then stop.
        """

        if (self.moving_state==self.MOVING_RIGHT):
            return

        self.moving_state = self.MOVING_RIGHT

        # Set motor speed and move both forward.
        self._left_speed(speed)
        self._right_speed(speed)
        self._left1.run(Adafruit_MotorHAT.FORWARD)
        self._left2.run(Adafruit_MotorHAT.FORWARD)
        self._right1.run(Adafruit_MotorHAT.BACKWARD)
        self._right2.run(Adafruit_MotorHAT.BACKWARD)
        # If an amount of time is specified, move for that time and then stop.
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def left(self, speed, seconds=None):
        """Spin to the left at the specified speed.  Will start spinning and
        return unless a seconds value is specified, in which case the robot will
        spin for that amount of time and then stop.
        """

        if (self.moving_state==self.MOVING_LEFT):
            return

        self.moving_state=self.MOVING_LEFT

        # Set motor speed and move both forward.
        self._left_speed(speed)
        self._right_speed(speed)
        self._left1.run(Adafruit_MotorHAT.BACKWARD)
        self._left2.run(Adafruit_MotorHAT.BACKWARD)
        self._right1.run(Adafruit_MotorHAT.FORWARD)
        self._right2.run(Adafruit_MotorHAT.FORWARD)
        # If an amount of time is specified, move for that time and then stop.
        if seconds is not None:
            time.sleep(seconds)
            self.stop()
