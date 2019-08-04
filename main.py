import argparse
import pygame
from pygame.mixer import Sound
import time
import glob
from random import choice
from aiy.board import Board, Led


# Init the pygame mixer
pygame.mixer.init()


def play_sound(filename, volume=1.0):
    sound_file = Sound(filename)
    sound_file.set_volume(volume)
    dur = sound_file.get_length()
    sound_file.play()
    time.sleep(dur)


def gen_file_list(directory):
    return tuple(glob.iglob(directory))


def play_random_sound(sound_list, volume=1.0):
    rand_choice = choice(sound_list)
    play_sound(rand_choice, volume)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=str)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    file_list = gen_file_list(args.directory)
    with Board() as board:
        board.led.state = Led.OFF
        while True:
            board.button.wait_for_press()
            board.led.state = Led.ON
            play_random_sound(file_list)
            board.led.state = Led.OFF
