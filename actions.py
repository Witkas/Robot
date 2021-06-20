# A module with actions that the robot performs.
import neopixels
from time import sleep
from threading import Thread
from sounds import play_sound

strip = neopixels.strip

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
        play_sound("R2D2_Excited_2.mp3")
        theater_chase(0, 0, 255)
        color_wipe(0, 0, 255)
        t_alive = False

    if t_alive:
        return
    else:
        Thread(target=inner).start()
    
# NeoPixel color wipe with a given RGB color.
def color_wipe(r, g, b):
    neopixels.colorWipe(strip, neopixels.Color(r, g, b))


# NeoPixel theater chase with a given RGB color.
def theater_chase(r, g, b):
    neopixels.theaterChase(strip, neopixels.Color(r, g, b))
