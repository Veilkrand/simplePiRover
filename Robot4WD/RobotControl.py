from Robot4WD.Robot4WD import Robot4WD


class RobotControl:

    LEFT_TRIM = 0
    RIGHT_TRIM = 0
    MIN_SPEED = 0.1  # [0, 1] absolute to start moving forward
    MIN_STEERING = 0.1  # [0, 1] Absolute to start turning
    MIN_SPEED_STEERING = 0.6  # [0, 1] absolute o switch from turning to steering
    robot = Robot4WD(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM,
                     left_id1=1,
                     left_id2=2,
                     right_id1=3,
                     right_id2=4)

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
