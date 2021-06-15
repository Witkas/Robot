import gpiozero
import time

class DistanceSensor:
    def __init__(self, TRIGGER, ECHO, max_distance=1):
        self.trigger = gpiozero.DigitalOutputDevice(TRIGGER)
        self.echo = gpiozero.DigitalInputDevice(ECHO)
        self.max_distance = max_distance
    # Returns the distance from the sensor in meters.
    def get_distance(self):
        # Trigger pulse
        self.trigger.on()
        time.sleep(0.00001)
        self.trigger.off()

        debugging_time = time.time()
        pulse_start = None
        pulse_end = None
        # Wait for the echo and measure its duration
        while self.echo.is_active == False:
            pulse_start = time.time()
            if pulse_start - debugging_time > 0.3:
                break
        while self.echo.is_active == True:
            pulse_end = time.time()
            if pulse_end - debugging_time > 0.3:
                break
        if pulse_start == None or pulse_end == None:
            return self.get_distance()
        pulse_duration = pulse_end - pulse_start # [s]
        SOUND_VELOCITY = 343 # [m/s]
        # Remember that the wave travels the distance twice
        distance = (SOUND_VELOCITY * pulse_duration / 2) # [m]
        if distance > self.max_distance:
            distance = self.max_distance
        distance = round(distance, 3)
        return distance



