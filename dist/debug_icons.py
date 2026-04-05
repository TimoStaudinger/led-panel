"""Debug script to preview all weather icons on the panel."""
import sys
import time

from rgbmatrix import RGBMatrix, RGBMatrixOptions

from rows.weather_icons import get_icon

PREVIEW_CODES = [0, 2, 3, 45, 61, 71, 95]

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.hardware_mapping = "adafruit-hat"
options.gpio_slowdown = 2

matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

try:
    for i, code in enumerate(PREVIEW_CODES):
        icon = get_icon(code)
        x_off = i * 9 + 1
        for x, y, r, g, b in icon:
            canvas.SetPixel(x_off + x, y, r, g, b)

    canvas = matrix.SwapOnVSync(canvas)
    print("All icons displayed. Ctrl+C to exit.")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    sys.exit(0)
