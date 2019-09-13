from Robot4WD import Robot4WD
from SimpleUDP.SimpleUDPServer import SimpleUDPServer

import time

# from numpy import interp

UDP_IP = "" ## Accept all IPs
UDP_PORT = 5005

server = SimpleUDPServer(UDP_IP, UDP_PORT)

LEFT_TRIM   = 0
RIGHT_TRIM  = 0

robot = Robot4WD(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM,left_id1=1,right_id1=2,left_id2=3,right_id2=4)

while True:

    inputs = server.listen()

    #print(inputs)

    
    """
    # To many polls to change motor speed. It has to run his own thread with suitable refresh. 
    # So it doens't try to change speed more than X times per second

    if inputs['buttons'][6]:
        axis=inputs['axis'][4]
        #speed=int(interp(axis,[-1,1],[0,255]))
        speed=int(interp(axis,[-1,1],[0,100]))
        robot.forward(1, None)
        robot._left_speed(speed)
        robot._right_speed(speed)

    elif inputs['buttons'][7]:
        robot.backward(50, None)
    else:
        robot.stop()

    """
    
    if inputs['axis'][2]<-0.5:
        robot.right(150,None)
    elif inputs['axis'][2]>0.5:
        robot.left(150,None)
    elif inputs['buttons'][6]:
        robot.forward(100, None)
    elif inputs['buttons'][7]:
        robot.backward(100, None)
    else:
        robot.stop()

    if inputs['buttons'][0]:
        print("STOP")
        robot.stop()
    
    #time.sleep(0.0001)

