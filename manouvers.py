from time import sleep
# Moves the robot back and then stops it.
def backtrack(robot, SPEED):
    robot.stop()
    sleep(0.1)
    robot.backward(SPEED)
    sleep(0.5)
    robot.stop()