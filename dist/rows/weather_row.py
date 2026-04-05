import os
import time

os.environ["TZ"] = "America/New_York"
time.tzset()

from rgbmatrix import graphics

from rows.weather_icons import get_icon
from weather import WeatherData

FONT_PATH = os.path.realpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "fonts", "tom-thumb.bdf")
)

# Right edges for right-aligned zones
ZONE_CURRENT = 38
ZONE_MAX = 56
ICON_X = 58  # 5px wide icon


def _text_width(font, text):
    return sum(font.CharacterWidth(ord(c)) for c in text)


class WeatherRow:
    def __init__(self):
        self.font = graphics.Font()
        self.font.LoadFont(FONT_PATH)

        self.white = graphics.Color(255, 255, 255)
        self.white_dim = graphics.Color(140, 140, 140)
        self.yellow = graphics.Color(255, 210, 0)
        self.yellow_dim = graphics.Color(140, 115, 0)
        self.dim = graphics.Color(200, 200, 200)

        self.y = 5  # baseline for tom-thumb font (ascent=5)
        self.height = 6

    def render(self, canvas, weather: WeatherData | None):
        time_str = time.strftime("%H:%M")
        graphics.DrawText(canvas, self.font, 0, self.y, self.dim, time_str)

        if weather is None:
            self._draw_placeholder(canvas)
            return

        current_num = str(weather.current_temp)
        max_num = str(weather.max_temp)

        # Current temp: number bright, degree dim
        deg_w = _text_width(self.font, "°")
        num_w = _text_width(self.font, current_num)
        cx = ZONE_CURRENT - deg_w - num_w
        graphics.DrawText(canvas, self.font, cx, self.y, self.white, current_num)
        graphics.DrawText(canvas, self.font, cx + num_w, self.y, self.white_dim, "°")

        # Max temp: arrow dim, number bright, degree dim
        max_num_w = _text_width(self.font, max_num)
        mx = ZONE_MAX - deg_w - max_num_w
        self._draw_up_arrow(canvas, mx - 4, self.yellow_dim)
        graphics.DrawText(canvas, self.font, mx, self.y, self.yellow, max_num)
        graphics.DrawText(canvas, self.font, mx + max_num_w, self.y, self.yellow_dim, "°")
        self._draw_icon(canvas, get_icon(weather.weather_code))

    def _draw_placeholder(self, canvas):
        self._draw_right(canvas, "--°", ZONE_CURRENT, self.dim)
        self._draw_right(canvas, "--°", ZONE_MAX, self.dim)

    def _draw_icon(self, canvas, icon):
        for x, y, r, g, b in icon:
            canvas.SetPixel(ICON_X + x, y, r, g, b)

    def _draw_up_arrow(self, canvas, x, color):
        r, g, b = color.red, color.green, color.blue
        canvas.SetPixel(x + 1, 1, r, g, b)
        canvas.SetPixel(x, 2, r, g, b)
        canvas.SetPixel(x + 1, 2, r, g, b)
        canvas.SetPixel(x + 2, 2, r, g, b)

    def _draw_right(self, canvas, text, right_edge, color):
        x = right_edge - _text_width(self.font, text)
        graphics.DrawText(canvas, self.font, x, self.y, color, text)
