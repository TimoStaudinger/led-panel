import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.hardware_mapping = "adafruit-hat"
options.gpio_slowdown = 2

matrix = RGBMatrix(options=options)

try:
    canvas = matrix.CreateFrameCanvas()

    # RGB gradient: red->green horizontal, blue vertical
    for x in range(64):
        for y in range(32):
            r = int(255 * (1 - x / 63))
            g = int(255 * (x / 63))
            b = int(255 * (y / 31))
            canvas.SetPixel(x, y, r, g, b)
    canvas = matrix.SwapOnVSync(canvas)

    print("Gradient displayed. Ctrl+C to exit.")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    sys.exit(0)
