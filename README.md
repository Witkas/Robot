# Robot
Presentation: https://www.youtube.com/watch?v=LkIvVDyR32E&ab_channel=Witkas <br>
## Project Description
This robot can be paired with a Wii remote controller (thanks to the [cwiid](https://github.com/azzra/python3-wiimote) library). <br><br>
When the program starts, it waits a short while for a connection from the remote. If devices pair succesfully, the robot's LEDs will turn blue and it will make a happy sound. Otherwise, LEDs turn off and an error is displayed. <br> 
The robot is capable of detecting obstacles in front of it using a ultrasonic sensor. When it detects one, it will make a beep, the LEDs will turn red for a brief moment, and the robot will back off a bit, waiting for other commands. <br>
Pressing the A button will make the robot play sounds and flash its LEDs.
## Hardware
* Raspberry Pi 3B+
* 8x AA Batteries
* 2x 5V DC Motor
* L293D Motor Controller
* LM2596 step-down Converter
* HC-SR04 Ultrasonic Sensor
* NeoPixel Stick
* Speaker
