from Robot4WD import Robot4WD


class RobotControl:

    LEFT_TRIM = 0
    RIGHT_TRIM = 0
    MIN_SPEED = 10  # [0, 255] to start moving forward
    MIN_SPEED_STEERING = 170  # [0, 255] To switch from turning to steering
    MIN_STEERING = 0.1  # [0, 1] To start turning
    robot = Robot4WD(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM,
                     left_id1=1,
                     left_id2=2,
                     right_id1=3,
                     right_id2=4)

    def __init__(self):
        pass

    def update(self, speed, steering):

        motor_power = int(speed * 255)

        if abs(motor_power) > self.MIN_SPEED_STEERING:
            self.robot.move_steering(motor_power, steering)
        else:
            if abs(steering) > self.MIN_STEERING:
                self.robot.turn(steering)
            elif abs(motor_power) > self.MIN_SPEED:
                self.robot.update_center(motor_power)
            else:
                self.robot.stop()

        print(motor_power, steering)
