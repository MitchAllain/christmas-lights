import numpy as np
from neopixel import *

import time

# LED strip configuration:
LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

def saturate_byte_list(vals):
    return [max(min(255, v), 0) for v in vals]

class LightEvent(object):
    '''A generic representation of an event with a duration and a trigger time

    Args:
        ts (float): Time to start event (seconds, rounding to nearest frame)
        duration (float): Duration of event (in seconds, also framerate rounded)

    Attributes:
        ts (float)
        dur (float)
        fs (int): start time in nearest frame number
        fdur (int): duration in number of frames
        pixels (np.array, floats): (fdur x 150 x 3) array of pixel values in (0, 255)
            '''
    def __init__(self, ts, duration):
        self.ts = ts
        self.fs = int(ts * 24)
        self.dur = duration
        self.fdur = int(duration * 24)
        self.pixels = np.zeros((self.fdur, 150, 3), dtype=np.int)

    def getFrameAtTime(self, t):
        ''' Returns a frame (150 x 3) array at playback time t '''
        return self.pixels[int((t - self.ts) / 24)]

    def getFrameAtNumber(self, fn):
        ''' Returns a frame (150 x 3) array at playback frame number fn '''
        return self.pixels[fn - self.fs]

class Bounce(LightEvent):
    '''A generic representation of an event with a duration and a trigger time

    Args:
        ts (float): Time to start event (seconds, rounding to nearest frame)
        duration (float): Duration of event (in seconds, also framerate rounded)

    Attributes:
        ts (float)
        dur (float)
        fs (int): start time in nearest frame number
        fdur (int): duration in number of frames
        pixels (np.array, floats): (fdur x 150 x 3) array of pixel values in (0, 255)
    '''

    def __init__(self, ts, duration, loc, color, radius):
        super(Bounce, self).__init__(ts, duration)
        self.loc = loc
        self.color = color
        self.radius = radius
        self._construct_pixels(loc, color, radius)

    def _construct_pixels(self, loc, color, radius):
        ''' Fill the pixels array. Two epicenters begin collocated,
            intensity decreases proportional to the square of distance from epicenter '''
        alpha = max(color) / float(radius ** 2)
        beta = (max(color) / float(self.fdur)) * 2
        gamma = 1.0
        # print("Alpha ", alpha)
        # print("Beta ", beta)
        # print("Gamma ", gamma)
        epimag = list(color)

        for i in range(self.fdur):
            epimag = saturate_byte_list([mag - beta for mag in epimag])
            # print(epimag)
            for j in range(150):
                epidist = min(abs(loc + (gamma * i) - j), abs(loc - (gamma * i) - j))
                pix = np.array(epimag) - alpha * epidist ** 2
                self.pixels[i, j] = np.clip(pix.astype(np.int), 0, 255)
                # if j == int(loc + gamma * i):
                    # print(epidist, self.pixels[i, j])
            # print("Frame %i: epicenters at %.2f, %.2f" % (i, loc + gamma * i, loc - gamma * i))


    def __repr__(self):
        return "Bounce(ts=%.2f, duration=%.2f, loc=%i, color=%s, radius=%i)" % (self.ts, self.dur, self.loc, self.color, self.radius)


# class PopFade(LightEvent):
    '''A generic representation of an event with a duration and a trigger time

    Args:
        ts (float): Time to start event (seconds, rounding to nearest frame)
        duration (float): Duration of event (in seconds, also framerate rounded)

    Attributes:
        ts (float)
        fs (int): start time in nearest frame number
        fdur (int): duration in number of frames
        pixels (np.array, floats): (fdur x 150 x 3) array of pixel values in (0, 255)
    '''


class EventSequence():
    def __init__(self, delay, length):
        self.delay = delay
        self.length = length
        self.frames = int(length * 24)
        self.pixels = np.zeros((self.frames, 150, 3), dtype=np.int)
        self.dt = 1.0 / 24

        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    def register_event(self, ev):
        print('New ' + ev.__repr__())
        assert (ev.pixels.shape[0] == ev.fdur)
        self.pixels[ev.fs:(ev.fdur + ev.fs)] += ev.pixels
        self.pixels = np.clip(self.pixels, 0, 255)

    def load_frame(self, i):
        for j in range(150):
            self.strip.setPixelColor(j, Color(*self.pixels[i, j]))
        self.strip.show()

    def run(self):
        time.sleep(self.delay)
        start = time.time()
        for i in range(len(self.pixels)):
            print time.time()
            self.load_frame(i)
            while time.time() < (start + (i * self.dt)):
                pass





