import sys
import time

from rgbmatrix import RGBMatrix, RGBMatrixOptions

from rows.weather_row import WeatherRow
from weather import fetch_weather

FETCH_INTERVAL = 300  # seconds

# Load fonts before RGBMatrix init — the constructor drops privileges
# from root to daemon, which blocks access to the home directory.
weather_row = WeatherRow()

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.hardware_mapping = "adafruit-hat"
options.gpio_slowdown = 2

matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

weather = None
last_fetch = 0

try:
    while True:
        now = time.time()
        if now - last_fetch >= FETCH_INTERVAL:
            result = fetch_weather()
            if result is not None:
                weather = result
            last_fetch = now

        canvas.Clear()
        weather_row.render(canvas, weather)
        canvas = matrix.SwapOnVSync(canvas)

        time.sleep(1)

except KeyboardInterrupt:
    sys.exit(0)
