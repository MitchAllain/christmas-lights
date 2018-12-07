import christmas_lights.events as lev

import argparse
import signal
import sys

import pygame

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

    test.register_event(lev.Bounce(0.893, 0.5, 20, (122, 122, 122), 30))
    # test.register_event(lev.Bounce(1.154, 2, 40, (122, 122, 122), 30))
    test.register_event(lev.Bounce(1.3, 0.5, 60, (122, 122, 122), 30))
    # test.register_event(lev.Bounce(1.75, 2, 100, (122, 122, 122), 30))
    # test.register_event(lev.Bounce(2.021, 2, 100, (122, 122, 122), 30))
    # test.register_event(lev.Bounce(2.291, 2, 100, (122, 122, 122), 30))
    # test.register_event(lev.Bounce(2.291, 2, 100, (122, 122, 122), 30))
    
    test.register_event(lev.Bounce(3.115, 1, 100, (122, 122, 122), 30))
    test.register_event(lev.Bounce(3.979, 1, 100, (122, 122, 122), 30))
    
    test.register_event(lev.Bounce(4.229, 1, 60, (122, 122, 122), 30))
    test.register_event(lev.Bounce(5.404, 1, 60, (122, 122, 122), 30))

    test.register_event(lev.Bounce(7.562, 1, 100, (122, 122, 122), 30))

    test.register_event(lev.Bounce(9.785,  1  , 75, (100, 0, 0), 10))
    test.register_event(lev.Bounce(10.341, 1  , 75, (122, 0, 0), 10))
    test.register_event(lev.Bounce(10.904, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(11.312, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(11.740, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(12.291, 1  , 115, (122, 0, 0), 10))
    test.register_event(lev.Bounce(12.729, 1  , 115, (122, 0, 0), 10))
    test.register_event(lev.Bounce(13.146, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(13.541, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(14.000, 1  , 40, (122, 0, 0), 10))

    test.register_event(lev.Bounce(14.235, 1  , 75, (122, 0, 0), 10))
    test.register_event(lev.Bounce(14.791,  1  , 75, (100, 0, 0), 10))
    test.register_event(lev.Bounce(15.342, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(15.764, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(16.187, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(16.757, 1  , 110, (122, 0, 0), 10))
    test.register_event(lev.Bounce(17.172, 1  , 110, (122, 0, 0), 10))
    test.register_event(lev.Bounce(17.562, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(17.985, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(18.404, 1  , 75, (122, 0, 0), 10))

    test.register_event(lev.Bounce(18.701, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(19.231, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(19.801, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(20.219, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(20.620, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(21.176, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(22.023, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(22.443, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(23.713, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(24.246, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(24.651, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(25.066, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(25.617, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(26.037, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(26.5, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(27.035, 1  , 40, (122, 0, 0), 10))
    test.register_event(lev.Bounce(27.301, 1  , 40, (122, 0, 0), 10))
    
    # Kicks begin here
    test.register_event(lev.Bounce(27.562, 1  , 40, (122, 0, 0), 10))

    pygame.mixer.init()
    pygame.mixer.music.load('light_it_up_audio.mp3')
    pygame.mixer.music.play()

    test.run()
