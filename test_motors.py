from Robot4WD.Robot4WD import Robot4WD

LEFT_TRIM = 0
RIGHT_TRIM = 0

robot = Robot4WD(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM, left_id1=1, right_id1=2, left_id2=3, right_id2=4)

robot.forward(50, 5)

#robot.left(50, 5)

#robot.right(50, 5)
