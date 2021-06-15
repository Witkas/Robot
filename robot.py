import gpiozero
import cwiid
import neopixels
import os
from threading import Thread
from distance_sensor import DistanceSensor
from manouvers import backtrack

# Hardware components of the project
robot = gpiozero.Robot(left=(23,24), right=(27,22))
sensor = DistanceSensor(25,9)
strip = neopixels.strip

SPEED = 1  # robot speed [0-1]


def play_sound_A():
    Thread(target=os.system, args=["mpg123 -q sounds/R2D2_Excited_2.mp3"]).start()
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
Thread(target = os.system, args = ["mpg123 -q sounds/R2D2_Excited.mp3"]).start()
# Turn on the reporting mode, which permits Python to read input from the Wiimote
wii.rpt_mode = cwiid.RPT_BTN

while True:
    try:
        distance = sensor.get_distance() * 100 # distance from the sensor to the obstacle [cm]
        sound_backtrack = Thread(target=os.system, args=["mpg123 -q sounds/R2D2_Snappy.mp3"])
        #sound_A = Thread(target=os.system, args=["mpg123 -q sounds/R2D2_Excited_2.mp3"])
        t = Thread(target=neopixels.theaterChase, args=[strip, neopixels.Color(0, 0, 255)])
        blue_wipe = Thread(target=neopixels.colorWipe, args=[strip, neopixels.Color(0, 0, 255)])
        red_wipe = Thread(target=neopixels.colorWipe, args=[strip, neopixels.Color(255, 0, 0), 10])
        
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
        if (buttons & cwiid.BTN_A):
            if not sound_A.is_alive():
                sound_A.start()
            #t.start()

        # Check the distance sensor
        if distance < 15: 
            red_wipe.start()
            sound_backtrack.start()
            backtrack(robot, SPEED)
            # Reset the NeoPixels
            distance = sensor.get_distance() * 100 # distance from the sensor to the obstacle [cm]
            if distance > 15:
                blue_wipe.start()
    except KeyboardInterrupt:
        neopixels.colorWipe(strip, neopixels.Color(0,0,0))
        exit()
