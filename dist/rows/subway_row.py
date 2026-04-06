import os

from rgbmatrix import graphics

from subway import Departure

FONT_PATH = os.path.realpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "fonts", "tom-thumb.bdf")
)

# Official MTA line colors (RGB)
LINE_COLORS = {
    "1": (238, 53, 46),
    "2": (238, 53, 46),
    "3": (238, 53, 46),
    "4": (0, 147, 60),
    "5": (0, 147, 60),
    "6": (0, 147, 60),
    "7": (185, 51, 173),
    "A": (0, 57, 166),
    "C": (0, 57, 166),
    "E": (0, 57, 166),
    "B": (255, 99, 25),
    "D": (255, 99, 25),
    "F": (255, 99, 25),
    "M": (255, 99, 25),
    "G": (108, 190, 69),
    "J": (153, 102, 51),
    "Z": (153, 102, 51),
    "L": (167, 169, 172),
    "N": (252, 204, 10),
    "Q": (252, 204, 10),
    "R": (252, 204, 10),
    "W": (252, 204, 10),
    "S": (128, 129, 131),
}

# Abbreviate long headsign text to fit the display
ABBREV = {
    "South Ferry": "S Ferry",
    "Coney Island-Stillwell Av": "Coney Is",
    "Bay Ridge-95 St": "95 St",
    "Whitehall St-South Ferry": "S Ferry",
    "Astoria-Ditmars Blvd": "Ditmars",
    "Flatbush Av-Brooklyn College": "Flatbush",
    "Far Rockaway-Mott Av": "Far Rock",
    "Wakefield-241 St": "241 St",
    "Harlem-148 St": "148 St",
    "Van Cortlandt Park-242 St": "242 St",
    "New Lots Av": "New Lots",
    "Crown Hts-Utica Av": "Utica Av",
    "Pelham Bay Park": "Pelham Bay",
    "Woodlawn": "Woodlawn",
    "Atlantic Av-Barclays Ctr": "Atlantic",
    "Jamaica Center-Parsons/Archer": "Jamaica",
    "Broad Channel": "Broad Ch",
    "Forest Hills-71 Av": "Forest Hls",
    "Middle Village-Metropolitan Av": "Metrop Av",
    "Flushing-Main St": "Flushing",
    "34 St-Hudson Yards": "Hudson Yds",
    "Canarsie-Rockaway Pkwy": "Canarsie",
    "Times Sq-42 St": "Times Sq",
    "Canal St": "Canal St",
}

# 5x5 pixel art for subway line letters — each is a set of (dx, dy) offsets
LETTER_PIXELS = {
    "1": {(1,0), (0,1),(1,1), (1,2), (1,3), (0,4),(1,4),(2,4)},
    "2": {(0,0),(1,0),(2,0), (3,1), (1,2),(2,2), (0,3), (0,4),(1,4),(2,4),(3,4)},
    "3": {(0,0),(1,0),(2,0),(3,0), (2,1), (1,2),(2,2), (3,3), (0,4),(1,4),(2,4),(3,4)},
    "4": {(0,0),(3,0), (0,1),(3,1), (0,2),(1,2),(2,2),(3,2), (3,3), (3,4)},
    "5": {(0,0),(1,0),(2,0),(3,0), (0,1), (0,2),(1,2),(2,2), (3,3), (0,4),(1,4),(2,4)},
    "6": {(1,0),(2,0), (0,1), (0,2),(1,2),(2,2), (0,3),(3,3), (1,4),(2,4)},
    "7": {(0,0),(1,0),(2,0),(3,0), (3,1), (2,2), (1,3), (1,4)},
    "A": {(1,0),(2,0), (0,1),(3,1), (0,2),(1,2),(2,2),(3,2), (0,3),(3,3), (0,4),(3,4)},
    "B": {(0,0),(1,0),(2,0), (0,1),(3,1), (0,2),(1,2),(2,2), (0,3),(3,3), (0,4),(1,4),(2,4)},
    "C": {(1,0),(2,0),(3,0), (0,1), (0,2), (0,3), (1,4),(2,4),(3,4)},
    "D": {(0,0),(1,0),(2,0), (0,1),(3,1), (0,2),(3,2), (0,3),(3,3), (0,4),(1,4),(2,4)},
    "E": {(0,0),(1,0),(2,0),(3,0), (0,1), (0,2),(1,2),(2,2), (0,3), (0,4),(1,4),(2,4),(3,4)},
    "F": {(0,0),(1,0),(2,0),(3,0), (0,1), (0,2),(1,2),(2,2), (0,3), (0,4)},
    "G": {(1,0),(2,0),(3,0), (0,1), (0,2),(2,2),(3,2), (0,3),(3,3), (1,4),(2,4),(3,4)},
    "J": {(3,0), (3,1), (3,2), (0,3),(3,3), (1,4),(2,4)},
    "L": {(0,0), (0,1), (0,2), (0,3), (0,4),(1,4),(2,4),(3,4)},
    "M": {(0,0),(3,0), (0,1),(1,1),(2,1),(3,1), (0,2),(1,2),(2,2),(3,2), (0,3),(3,3), (0,4),(3,4)},
    "N": {(0,0),(3,0), (0,1),(3,1), (0,2),(1,2),(3,2), (0,3),(2,3),(3,3), (0,4),(3,4)},
    "Q": {(1,0),(2,0), (0,1),(3,1), (0,2),(3,2), (0,3),(2,3), (1,4),(2,4),(3,4)},
    "R": {(0,0),(1,0),(2,0), (0,1),(3,1), (0,2),(1,2),(2,2), (0,3),(2,3), (0,4),(3,4)},
    "S": {(1,0),(2,0),(3,0), (0,1), (1,2),(2,2), (3,3), (0,4),(1,4),(2,4)},
    "W": {(0,0),(3,0), (0,1),(3,1), (0,2),(1,2),(2,2),(3,2), (0,3),(1,3),(2,3),(3,3), (0,4),(3,4)},
    "Z": {(0,0),(1,0),(2,0),(3,0), (3,1), (1,2),(2,2), (0,3), (0,4),(1,4),(2,4),(3,4)},
}

# Layout constants
FIRST_ROW_Y = 12  # baseline for first subway row (after weather + 1px gap)
ROW_SPACING = 6  # tom-thumb font height
LINE_X = 0  # line letter
DEST_X = 6  # destination text start (after 4px letter + 2px gap)
MINUTES_RIGHT = 63  # right edge for minutes


def _text_width(font, text):
    return sum(font.CharacterWidth(ord(c)) for c in text)


class SubwayRow:
    def __init__(self):
        self.font = graphics.Font()
        self.font.LoadFont(FONT_PATH)

        self.white = graphics.Color(255, 255, 255)
        self.station_color = graphics.Color(130, 130, 130)
        self.dest_color = graphics.Color(0, 100, 160)

    def render(self, canvas, departures: list[Departure] | None):
        if not departures:
            return

        for i, dep in enumerate(departures):
            y = FIRST_ROW_Y + i * ROW_SPACING
            self._draw_departure(canvas, y, dep)

    def _draw_departure(self, canvas, y, dep: Departure):
        # Line letter as 5x5 pixel art in MTA color
        r, g, b = LINE_COLORS.get(dep.line, (200, 200, 200))
        top = y - 4  # align top of 5x5 art with top of text row
        pixels = LETTER_PIXELS.get(dep.line)
        if pixels:
            for dx, dy in pixels:
                canvas.SetPixel(LINE_X + dx, top + dy, r, g, b)
        else:
            # Fallback to font for unknown letters
            line_color = graphics.Color(r, g, b)
            graphics.DrawText(canvas, self.font, LINE_X, y, line_color, dep.line)

        # Station label
        graphics.DrawText(canvas, self.font, DEST_X, y, self.station_color, dep.station)
        dest_x = DEST_X + _text_width(self.font, dep.station) + 2

        # Minutes (right-aligned)
        min_str = "now" if dep.minutes == 0 else f"{dep.minutes}m"
        min_w = _text_width(self.font, min_str)
        min_x = MINUTES_RIGHT - min_w + 1
        graphics.DrawText(canvas, self.font, min_x, y, self.white, min_str)

        # Destination (truncated to fit between station label and minutes)
        dest = ABBREV.get(dep.destination, dep.destination)
        max_dest_w = min_x - dest_x - 2  # 2px gap before minutes
        while dest and _text_width(self.font, dest) > max_dest_w:
            dest = dest[:-1]
        if dest:
            graphics.DrawText(canvas, self.font, dest_x, y, self.dest_color, dest)
