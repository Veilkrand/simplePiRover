import time
import atexit

from Adafruit_MotorHAT import Adafruit_MotorHAT
from adafruit_motorkit import MotorKit


class Robot4WD(object):

    #handling states
    STOP = 0
    MOVING_FORWARD = 1
    MOVING_BACKWARD = 2
    MOVING_LEFT = 3
    MOVING_RIGHT = 4
    moving_state = STOP

    def __init__(self, addr=0x60, left_id1=1, right_id1=2, left_id2=3, right_id2=4,
                 left_trim=0, right_trim=0,
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

        self.left_trim = left_trim
        self.right_trim = right_trim

        self.kit = MotorKit()

        # Configure all motors to stop at program exit if desired.
        if stop_at_exit:
            atexit.register(self.stop)

    def _left_speed(self, speed):

        _motor_speed = max(-1, min(1, speed + self.left_trim))  # Constrain speed to [-1,1] after trimming.

        self.kit.motor1.throttle = _motor_speed
        self.kit.motor2.throttle = _motor_speed

    def _right_speed(self, speed):

        _motor_speed = max(-1, min(1, speed + self.right_trim))  # Constrain speed to [-1,1] after trimming.

        self.kit.motor3.throttle = _motor_speed
        self.kit.motor4.throttle = _motor_speed

    def stop(self):
        """Stop all movement. release the motors"""

        self.moving_state = self.STOP

        self.kit.motor1.throttle = None
        self.kit.motor2.throttle = None
        self.kit.motor3.throttle = None
        self.kit.motor4.throttle = None

    def brake(self):

        self.moving_state = self.STOP

        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0
        self.kit.motor3.throttle = 0
        self.kit.motor4.throttle = 0

    def move_steering(self, speed, steering):
        """
        :param speed: -1, 1
        :param steering: -1, 1
        :return:
        """

        _left_speed = speed
        _right_speed = speed

        if steering > 0:  # turning right
            _right_speed = _right_speed - (_right_speed * abs(steering))
        elif steering < 0:  # turning left
            _left_speed = _left_speed - (_left_speed * abs(steering))

        self._left_speed(_left_speed)
        self._right_speed(_right_speed)

    def turn(self, steering):
        """

        :param steering: -1, 1
        :return:
        """

        self._left_speed(steering)
        self._right_speed(-steering)


    def move(self, speed):
        """Forward or backward in realtime"""

        self._left_speed(speed)
        self._right_speed(speed)

    # ---

    def forward(self, speed, seconds=None):
        """Move forward at the specified speed (0-255).  Will start moving
        forward and return unless a seconds value is specified, in which
        case the robot will move forward for that amount of time and then stop.
        """

        if (self.moving_state==self.MOVING_FORWARD):
            return

        self.moving_state = self.MOVING_FORWARD

        # Set motor speed and move both forward.
        self.move(speed)
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

        self.moving_state = self.MOVING_BACKWARD

        # Set motor speed and move both backward.
        self.move(-speed)
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
        self.turn(speed)
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

        self.turn(-speed)
        # If an amount of time is specified, move for that time and then stop.
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

