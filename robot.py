import gpiozero
import cwiid
import neopixels
from threading import Thread
from distance_sensor import DistanceSensor
from manouvers import backtrack
from sounds import happy_sound_1, happy_sound_2, angry_sound_1

# Hardware components of the project
robot = gpiozero.Robot(left=(23,24), right=(27,22))
sensor = DistanceSensor(25,9)
strip = neopixels.strip

SPEED = 1  # robot speed [0-1]

def play_sound_A():
    happy_sound_2()
    neopixels.theaterChase(strip, neopixels.Color(0, 0, 255))
    # Reset the Thread
    neopixels.colorWipe(strip, neopixels.Color(0, 0, 255))
    global sound_A
    sound_A = Thread(target=play_sound_A)

sound_A = Thread(target=play_sound_A)
# MAIN PROGRAM
# Making connection with the Wiimote
print("Press and hold the 1+2 buttons on your Wiimote simultaneously.")
neopixels.colorWipe(strip, neopixels.Color(0, 100, 60))
try:    
    wii = cwiid.Wiimote()
except RuntimeError:
    neopixels.colorWipe(strip, neopixels.Color(0,0,0))
    exit()
print("Connection established.")
neopixels.colorWipe(strip, neopixels.Color(0, 0, 255))
happy_sound_1()
# Turn on the reporting mode, which permits Python to read input from the Wiimote
wii.rpt_mode = cwiid.RPT_BTN

while True:
    try:
        # Wiimote controls
        buttons = wii.state["buttons"]
        if (buttons & cwiid.BTN_LEFT):  # Press LEFT
            robot.left(SPEED)
        if (buttons & cwiid.BTN_RIGHT): # Press RIGHT
            robot.right(SPEED)
        if (buttons & cwiid.BTN_UP):    # Press UP
            robot.forward(SPEED)
        if (buttons & cwiid.BTN_DOWN):  # Press DOWN
            robot.backward(SPEED)
        if (buttons & cwiid.BTN_B):     # Press B
            robot.stop()
        if (buttons & cwiid.BTN_A):     # Press A
            if not sound_A.is_alive():
                sound_A.start()

        # Check the distance sensor
        distance = sensor.get_distance() # distance from the sensor to the obstacle [cm]
        blue_wipe = Thread(target=neopixels.colorWipe, args=[strip, neopixels.Color(0, 0, 255)])
        red_wipe = Thread(target=neopixels.colorWipe, args=[strip, neopixels.Color(255, 0, 0), 10])
        if distance < 15: 
            red_wipe.start()
            angry_sound_1()
            backtrack(robot, SPEED)
            # Reset the NeoPixels
            distance = sensor.get_distance() # distance from the sensor to the obstacle [cm]
            if distance > 15:
                blue_wipe.start()
    except KeyboardInterrupt:
        neopixels.colorWipe(strip, neopixels.Color(0,0,0))
        exit()
