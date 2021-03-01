import time
import atexit

from adafruit_motorkit import MotorKit


class Robot4WD(object):

    #handling states
    STOP = 0
    MOVING_FORWARD = 1
    MOVING_BACKWARD = 2
    MOVING_LEFT = 3
    MOVING_RIGHT = 4
    moving_state = STOP

    def __init__(self, address=0x60,
                 left_id1=1, right_id1=2, left_id2=3, right_id2=4,
                 left1_trim=0, left2_trim=0, right1_trim=0, right2_trim=0
                 ):
        """Create an instance of the robot.  Can specify the following optional
        parameters:
         - addr: The I2C address of the motor HAT, default is 0x60.
         - left_trim: Amount to offset the speed of the left motor, can be positive
                      or negative and use useful for matching the speed of both
                      motors.  Default is 0.
         - right_trim: Amount to offset the speed of the right motor (see above).
         - stop_at_exit: Boolean to indicate if the motors should stop on program
                         exit.  Default is True (highly recommended to keep this
                         value to prevent damage to the bot on program crash!).
        """

        self.left1_trim = left1_trim
        self.left2_trim = left2_trim
        self.right1_trim = right1_trim
        self.right2_trim = right2_trim

        self.kit = MotorKit(address=address)

        self.motor_left1 = self.kit.motor1
        self.motor_left2 = self.kit.motor2
        self.motor_right1 = self.kit.motor3
        self.motor_right2 = self.kit.motor4

        # Configure all motors to stop at program exit if desired.
        atexit.register(self.stop)

    def _left_speed(self, speed):

        _motor_speed1 = max(-1.0, min(1.0, speed + self.left1_trim))  # Constrain speed to [-1,1] after trimming.
        _motor_speed2 = max(-1.0, min(1.0, speed + self.left2_trim))  # Constrain speed to [-1,1] after trimming.

        self.motor_left1.throttle = _motor_speed1
        self.motor_left2.throttle = _motor_speed2

    def _right_speed(self, speed):

        _motor_speed1 = max(-1.0, min(1.0, speed + self.right1_trim))  # Constrain speed to [-1,1] after trimming.
        _motor_speed2 = max(-1.0, min(1.0, speed + self.right2_trim))  # Constrain speed to [-1,1] after trimming.

        self.motor_right1.throttle = _motor_speed1
        self.motor_right2.throttle = _motor_speed2

    def stop(self):
        """Stop all movement. release the motors"""

        self.moving_state = self.STOP

        self.motor_left1.throttle = None
        self.motor_left2.throttle = None
        self.motor_right1.throttle = None
        self.motor_right2.throttle = None

    def brake(self):

        self.moving_state = self.STOP

        self.motor_left1.throttle = 0
        self.motor_left2.throttle = 0
        self.motor_right1.throttle = 0
        self.motor_right2.throttle = 0

    def move_steering(self, speed, steering):
        """
        :param speed: -1, 1
        :param steering: -1, 1
        :return:
        """


        if steering > 0:  # turning right
            _left_speed = speed + (speed * steering * 1.4)
            _right_speed = speed - (speed * steering * 1.4)
        elif steering < 0:  # turning left
            _left_speed = speed - (speed * -steering * 1.4)
            _right_speed = speed + (speed * -steering * 1.4)
        else:
            _left_speed = speed
            _right_speed = speed


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

