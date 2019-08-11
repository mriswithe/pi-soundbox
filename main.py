import argparse
import subprocess

import pygame
from pygame.mixer import Sound
import time
import glob
from random import choice
import os
from aiy.board import Board, Led

SHUTDOWN_FILENAME = 'shutdown.ogg'
STARTUP_FILENAME = 'startup.ogg'
RUNPATH = os.path.dirname(os.path.realpath(__file__))
SHUTDOWN_PATH = RUNPATH + '/' + SHUTDOWN_FILENAME
STARTUP_PATH = RUNPATH + '/' + STARTUP_FILENAME
SHUTDOWN_SOUND = None
SHUTDOWN_DUR = None
STARTUP_SOUND = None
STARTUP_DUR = None
VOLUME=0.8

def prep_shutdown_sound():
    global SHUTDOWN_SOUND
    global SHUTDOWN_DUR
    SHUTDOWN_SOUND = Sound(SHUTDOWN_PATH)
    SHUTDOWN_SOUND.set_volume(.1)
    SHUTDOWN_DUR = SHUTDOWN_SOUND.get_length()

def prep_startup_sound():
    global STARTUP_SOUND
    global STARTUP_DUR
    STARTUP_SOUND = Sound(STARTUP_PATH)
    STARTUP_DUR = STARTUP_SOUND.get_length()

def play_sound(sound_file, volume=1.0):
    dur = sound_file.get_length()
    sound_file.play()
    time.sleep(dur)


def gen_file_list(directory):
    return tuple(glob.iglob(directory + '/*'))


def prep_sound_file(sound_list, volume=1.0):
    rand_choice = choice(sound_list)
    rand_sound = Sound(rand_choice)
    rand_sound.set_volume(volume)
    return rand_sound


def arg_parse_setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=str)
    return parser.parse_args()


def signal_ready(board):
    play_sound(STARTUP_SOUND)
    for i in range(5):
        board.led.state = Led.ON
        time.sleep(.2)
        board.led.state = Led.OFF
        time.sleep(.2)


if __name__ == '__main__':
    # Init the pygame mixer
    pygame.mixer.init()
    prep_startup_sound()
    prep_shutdown_sound()
    args = arg_parse_setup()
    with Board() as board:
        signal_ready(board)

        board.led.state = Led.OFF
        while True:
            file_list = gen_file_list(args.directory)
            next_sound = prep_sound_file(file_list, volume=VOLUME)
            board.button.wait_for_press()
            out = board.button.wait_for_release(5)
            if out:
                board.led.state = Led.ON
                play_sound(next_sound)
                board.led.state = Led.OFF
            else:
                print('Button held for 5 seconds, shutting down')
                board.led.state = Led.ON
                SHUTDOWN_SOUND.play()
                time.sleep(SHUTDOWN_DUR)
                subprocess.call(['/sbin/poweroff'])
                time.sleep(1000)
