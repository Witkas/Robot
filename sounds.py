# Module responsible for playing sounds, abstracting it from the main program.

from threading import Thread
from os import system


def happy_sound_1():
    Thread(target=system, args=["mpg123 -q sounds/R2D2_Excited.mp3"]).start()


def happy_sound_2():
    Thread(target=system, args=["mpg123 -q sounds/R2D2_Excited_2.mp3"]).start()


def angry_sound_1():
    Thread(target=system, args=["mpg123 -q sounds/R2D2_Snappy.mp3"]).start()