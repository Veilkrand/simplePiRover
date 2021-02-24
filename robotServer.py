from Robot4WD.Robot4WD import RobotControl
from PanTilt.PanTilt import PanTiltController
from SimpleUDP.SimpleUDPServer import SimpleUDPServer

import time

# from numpy import interp

UDP_IP = "" ## Accept all IPs
UDP_PORT = 5005

server = SimpleUDPServer(UDP_IP, UDP_PORT)

# robot = Robot4WD(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM, left_id1=1, right_id1=2, left_id2=3, right_id2=4)
robot = RobotControl()
pt = PanTiltController()

while True:

    inputs = server.listen()

    axis_speed = inputs['axis'][5]
    axis_steering = inputs['axis'][2]

    axis_pan = -inputs['axis'][0]
    axis_tilt = inputs['axis'][1]

    hat_x = -inputs['hat'][0] * 2
    hat_y = -inputs['hat'][1] * 2

    robot.update(axis_speed, axis_steering)

    pt.update_center(hat_x, hat_y)
    pt.look(axis_pan, axis_tilt)

    # time.sleep(0.001)

