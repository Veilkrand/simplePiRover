from Robot4WD.RobotControl import RobotControl
from PanTilt.PanTilt import PanTiltController
from SimpleUDP.SimpleUDPServer import SimpleUDPServer
# import time
# from numpy import interp

if __name__ == "__main__":

    UDP_IP = ""  # Accept all IPs
    UDP_PORT = 5005

    server = SimpleUDPServer(UDP_IP, UDP_PORT)

    robot = RobotControl()
    pt = PanTiltController()

    while True:

        inputs = server.listen()

        axis_speed = inputs['axis'][5]
        axis_steering = inputs['axis'][2]

        axis_pan = -inputs['axis'][0]
        axis_tilt = inputs['axis'][1]

        hat_x = -inputs['hat'][0]
        hat_y = -inputs['hat'][1]

        robot.update(axis_speed, axis_steering)

        pt.update_center(hat_x, hat_y)
        pt.look(axis_pan, axis_tilt)

        # client is already throttled down, there's no need to do it here. We need to process incoming packets as soon
        # as possible.
        # time.sleep(0.001)