import sys
import time

from rgbmatrix import RGBMatrix, RGBMatrixOptions

from rows.weather_row import WeatherRow
from rows.subway_row import SubwayRow
from weather import fetch_weather
from subway import fetch_subway

WEATHER_FETCH_INTERVAL = 300  # seconds
SUBWAY_FETCH_INTERVAL = 30  # seconds

# Load fonts before RGBMatrix init — the constructor drops privileges
# from root to daemon, which blocks access to the home directory.
weather_row = WeatherRow()
subway_row = SubwayRow()

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.hardware_mapping = "adafruit-hat"
options.gpio_slowdown = 2

matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

weather = None
last_weather_fetch = 0
departures = None
last_subway_fetch = 0

try:
    while True:
        now = time.time()
        if now - last_weather_fetch >= WEATHER_FETCH_INTERVAL:
            result = fetch_weather()
            if result is not None:
                weather = result
                last_weather_fetch = now

        if now - last_subway_fetch >= SUBWAY_FETCH_INTERVAL:
            result = fetch_subway()
            if result is not None:
                departures = result
                last_subway_fetch = now

        canvas.Clear()
        weather_row.render(canvas, weather)
        subway_row.render(canvas, departures)
        canvas = matrix.SwapOnVSync(canvas)

        time.sleep(5)

except KeyboardInterrupt:
    sys.exit(0)
