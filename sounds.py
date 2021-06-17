# Module responsible for playing sounds, abstracting it from the main program.
from threading import Thread
from os import system


def play_sound(name: str) -> None:
    Thread(target=system, args=[f"mpg123 -q sounds/{name}"]).start()