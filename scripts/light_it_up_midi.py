import christmas_lights.events as lev

import argparse
import signal
import sys

import pygame
import pandas as pd

def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    # Process arguments
    opt_parse()

    test = lev.EventSequence(0.6, 30.0)
    midi = pd.read_csv('light_it_up.csv')
    times = midi[midi['on_off'] == ' Note_on_c'].values[:, 0]

    for i in range(len(times)):
        test.register_event(lev.Bounce(midi[i] / 1000.0, 0.5, 
            np.random.randint(10, 140), (122, 122, 122), 30))

    pygame.mixer.init()
    pygame.mixer.music.load('light_it_up_audio.mp3')
    pygame.mixer.music.play()

    test.run()
