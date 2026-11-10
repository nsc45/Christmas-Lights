import board
import neopixel
import time

# Configure the setup
PIXEL_PIN = board.GP0  # pin that the NeoPixel is connected to
ORDER = neopixel.RGB  # pixel color channel order
COLOR = (255, 50, 150)  # color to blink
CLEAR = (0, 0, 0)  # clear (or second color)
DELAY = 0.1  # blink rate in seconds

# Create the NeoPixel object
num_pixels = 30
pixel_seg = neopixel.NeoPixel(PIXEL_PIN, num_pixels, pixel_order=ORDER)
pixel_seg.fill(CLEAR)

# Final strip configuration
PIXEL_PIN = board.GP0  # green cable plugged in
NUM_PIXELS = 30
PIXEL_BRIGHTNESS = 0.5

# Create object
strip = neopixel.NeoPixel(
    PIXEL_PIN,
    NUM_PIXELS,
    brightness=PIXEL_BRIGHTNESS,
    auto_write=False
)


def pixel_colour():
    strip.fill((0, 250, 0))  # green
    strip.show()


def set_pixel_index(index):
    for i in range(strip.n):
        strip[i] = (0, 250, 0) if i == index else (10, 0, 0)
    strip.show()

""" strip.fill((0, 250, 0))  # green
strip.show() """

while True:
    for i in range(NUM_PIXELS - 1):
        set_pixel_index(i)
        time.sleep(0.1 * (i / NUM_PIXELS))

    for i in range(NUM_PIXELS - 1, 0, -1):
        set_pixel_index(i)
        time.sleep(0.1 * (i / NUM_PIXELS))
    #print("hello")