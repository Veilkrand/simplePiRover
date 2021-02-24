from Robot4WD.Robot4WD import Robot4WD


class RobotControl:

    LEFT1_TRIM = 0
    LEFT2_TRIM = 0
    RIGHT1_TRIM = 0
    RIGHT2_TRIM = 0
    MIN_SPEED = 0.25  # [0, 1] absolute to start moving forward
    MIN_STEERING = 0.1  # [0, 1] Absolute to start turning
    MIN_SPEED_STEERING = 0.5  # [0, 1] absolute o switch from turning to steering
    robot = Robot4WD(left1_trim=LEFT1_TRIM, right1_trim=RIGHT1_TRIM,
                     left2_trim=LEFT2_TRIM, right2_trim=RIGHT2_TRIM,
                     )

    def __init__(self):
        pass

    def update(self, speed, steering):

        if abs(speed) > self.MIN_SPEED_STEERING:
            self.robot.move_steering(speed, steering)
        else:
            if abs(steering) > self.MIN_STEERING:
                self.robot.turn(steering)
            elif abs(speed) > self.MIN_SPEED:
                self.robot.move(speed)
            else:
                self.robot.stop()

        print(speed, steering)
