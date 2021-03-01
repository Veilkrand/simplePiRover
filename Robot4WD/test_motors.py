from Robot4WD import Robot4WD

LEFT_TRIM = 0
RIGHT_TRIM = 0

print("Running forward for 5 seconds...")
robot = Robot4WD(left1_trim=0, left2_trim=0, right1_trim=0, right2_trim=0)

robot.forward(0.5, 5)

#robot.left(0.5, 5)

#robot.right(0.5, 5)

print("Done.")