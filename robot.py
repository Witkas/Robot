import gpiozero
import cwiid
import neopixels
from threading import Thread
from distance_sensor import DistanceSensor
from actions import go_back, action_A, color_wipe
from sounds import play_sound

# Hardware components of the project
robot = gpiozero.Robot(left=(23,24), right=(27,22))
sensor = DistanceSensor(25,9)
strip = neopixels.strip

SPEED = 1  # robot speed [0-1]

# Making connection with the Wiimote
print("Press and hold the 1+2 buttons on your Wiimote simultaneously.")
color_wipe(0, 100, 60)
try:    
    wii = cwiid.Wiimote()
except RuntimeError:
    color_wipe(0, 0, 0)
    exit()
print("Connection established.")
color_wipe(0, 0, 255)
play_sound("R2D2_Excited.mp3")
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
            action_A()

        # Check the distance sensor
        distance = sensor.get_distance() # distance from the sensor to the obstacle [cm]
        blue_wipe = Thread(target=color_wipe, args=[0, 0, 255])
        red_wipe = Thread(target=color_wipe, args=[255, 0, 0, 10])
        if distance < 15: 
            red_wipe.start()
            play_sound("R2D2_Snappy.mp3")
            go_back(robot, SPEED)
            # Reset the NeoPixels
            distance = sensor.get_distance() # distance from the sensor to the obstacle [cm]
            if distance > 15:
                blue_wipe.start()
    except KeyboardInterrupt:
        color_wipe(0, 0, 0)
        exit()
