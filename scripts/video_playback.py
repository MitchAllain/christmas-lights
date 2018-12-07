# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *
import pickle
# import pygame

import argparse
import signal
import sys
def signal_handler(signal, frame):
    colorWipe(strip, Color(0,0,0))
    sys.exit(0)

def opt_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='clear the display on exit')
    parser.add_argument('input_file', help='input array of pixel values')
    parser.add_argument('audio_file', help='audio file to play')
    args = parser.parse_args()
    if args.c:
        signal.signal(signal.SIGINT, signal_handler)
    return args.input_file, args.audio_file

# LED strip configuration:
LED_COUNT      = 150     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10     # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

def validate_vid_array(px):
    return True

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def load_frame(strip, pix_bgr):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(int(pix_bgr[i][2]), 
                                     int(pix_bgr[i][0]),
                                     int(pix_bgr[i][1])))
    strip.show()


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    fn, afn = opt_parse()
    with open(fn, 'rb') as pklread:
        px = pickle.load(pklread)

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    if not validate_vid_array(px):
        print("Invalid input file...")
        sys.exit()

    # pygame.mixer.init()
    # pygame.mixer.music.load(afn)
    # pygame.mixer.music.play()

    print ('Press Ctrl-C to quit.')
    # st = time.time()
    # loop = time.time()
    last = time.time()
    while True:
        for i in range(len(px)):
            # loop = time.time()
            # st = time.time()
            load_frame(strip, px[i])
            # while time.time() < (((1 / 24.0) * i) + st):
            while (time.time() - last < 0.04166666):
                pass
            print(time.time() - last)
            last = time.time()
