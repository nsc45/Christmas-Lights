print("Press Ctrl-C to quit.")

import time
import board
import neopixel

PIXEL_PIN = board.GP1
NUM_PIXELS = 30   #for the short strip lights
# NUM_PIXELS = 256    #for the rectangle lights
BRIGHTNESS = 0.5
# DIM_GREEN = (0, 10, 0)
# RED = (250, 0, 0)
DIM_RED = (10, 0, 0)
DIM_WHITE = (10, 10, 10)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)
STEP_DELAY = 0.1

strip = neopixel.NeoPixel(
    PIXEL_PIN,
    NUM_PIXELS,
    brightness=BRIGHTNESS,
    auto_write=False,
)

def set_pixel_index(index):
    for pixel in range(NUM_PIXELS):
        # strip[pixel] = RED if pixel == index else DIM_GREEN
        strip[pixel] = GREEN if pixel == index else (DIM_RED if pixel % 2 == 0 else DIM_WHITE)
    strip.show()

try:
    strip.fill(OFF)
    strip.show()

    while True:
        for index in range(NUM_PIXELS):
            set_pixel_index(index)
            time.sleep(STEP_DELAY)

        for index in range(NUM_PIXELS - 2, 0, -1):
            set_pixel_index(index)
            time.sleep(STEP_DELAY)
except KeyboardInterrupt:
    strip.fill(OFF)
    strip.show()
