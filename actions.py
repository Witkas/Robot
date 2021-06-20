# A module with actions that the robot performs.
import neopixels
from time import sleep
from threading import Thread
from sounds import play_sound

# Moves the robot back and then stops it.
def go_back(robot, SPEED):
    robot.stop()
    sleep(0.1)
    robot.backward(SPEED)
    sleep(0.5)
    robot.stop()


# Play sound and flash LEDs when A on the Wiimote is pressed.
t_alive = False # Keep track whether the action is currently active
def action_A():
    def inner():
        global t_alive
        t_alive = True
        strip = neopixels.strip
        play_sound("R2D2_Excited_2.mp3")
        neopixels.theaterChase(strip, neopixels.Color(0, 0, 255))
        # Reset the Thread
        neopixels.colorWipe(strip, neopixels.Color(0, 0, 255))
        t_alive = False

    global t_alive
    if t_alive:
        return
    else:
        Thread(target=inner).start()
    