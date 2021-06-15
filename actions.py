# A module with actions that the robot performs.
from time import sleep
from sounds import happy_sound_2

# Moves the robot back and then stops it.
def go_back(robot, SPEED):
    robot.stop()
    sleep(0.1)
    robot.backward(SPEED)
    sleep(0.5)
    robot.stop()

# This happens when A on the Wiimote is pressed.
def action_A():
    pass