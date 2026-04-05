# 5x5 pixel art weather icons.
# Each icon is a list of (x, y, r, g, b) tuples relative to top-left origin.

Y = (255, 210, 0)      # warm yellow (sun)
W = (255, 255, 255)     # white (snow/highlights)
G = (130, 130, 130)     # gray (cloud)
D = (80, 80, 80)        # dark gray (cloud shadow)
B = (0, 150, 255)       # blue (rain)
L = (100, 100, 200)     # light blue (fog)
O = (255, 200, 0)       # orange (lightning)

_SUN = [
    #   * * *
    # * * * * *
    # * * * * *
    # * * * * *
    #   * * *
    (1, 0, *Y), (2, 0, *Y), (3, 0, *Y),
    (0, 1, *Y), (1, 1, *Y), (2, 1, *Y), (3, 1, *Y), (4, 1, *Y),
    (0, 2, *Y), (1, 2, *Y), (2, 2, *Y), (3, 2, *Y), (4, 2, *Y),
    (0, 3, *Y), (1, 3, *Y), (2, 3, *Y), (3, 3, *Y), (4, 3, *Y),
    (1, 4, *Y), (2, 4, *Y), (3, 4, *Y),
]

_PARTLY_CLOUDY = [
    # * *
    # * * * *
    #   * * * *
    # * * * * *
    #
    (0, 0, *Y), (1, 0, *Y),
    (0, 1, *Y), (1, 1, *Y), (2, 1, *G), (3, 1, *G),
    (1, 2, *G), (2, 2, *G), (3, 2, *G), (4, 2, *G),
    (0, 3, *D), (1, 3, *D), (2, 3, *D), (3, 3, *D), (4, 3, *D),
]

_CLOUDY = [
    #
    #     * *
    #   * * * *
    # * * * * *
    #
    (2, 1, *G), (3, 1, *G),
    (1, 2, *G), (2, 2, *G), (3, 2, *G), (4, 2, *G),
    (0, 3, *D), (1, 3, *D), (2, 3, *D), (3, 3, *D), (4, 3, *D),
]

_RAIN = [
    #     * *
    #   * * * *
    # * * * * *
    #   *   *
    # *   *
    (2, 0, *G), (3, 0, *G),
    (1, 1, *G), (2, 1, *G), (3, 1, *D), (4, 1, *D),
    (0, 2, *G), (1, 2, *D), (2, 2, *D), (3, 2, *D), (4, 2, *D),
    (1, 3, *B), (3, 3, *B),
    (0, 4, *B), (2, 4, *B),
]

_SNOW = [
    #     * *
    #   * * * *
    # * * * * *
    # *   *   *
    #   *   *
    (2, 0, *G), (3, 0, *G),
    (1, 1, *G), (2, 1, *G), (3, 1, *D), (4, 1, *D),
    (0, 2, *G), (1, 2, *D), (2, 2, *D), (3, 2, *D), (4, 2, *D),
    (0, 3, *W), (2, 3, *W), (4, 3, *W),
    (1, 4, *W), (3, 4, *W),
]

_FOG = [
    # * * * * *
    #
    #   * * * *
    #
    # * * * *
    (0, 0, *L), (1, 0, *L), (2, 0, *L), (3, 0, *L), (4, 0, *L),
    (1, 2, *L), (2, 2, *L), (3, 2, *L), (4, 2, *L),
    (0, 4, *L), (1, 4, *L), (2, 4, *L), (3, 4, *L),
]

_THUNDERSTORM = [
    #     * *
    #   * * * *
    # * * * * *
    #     * *
    #   *
    (2, 0, *G), (3, 0, *G),
    (1, 1, *G), (2, 1, *G), (3, 1, *D), (4, 1, *D),
    (0, 2, *G), (1, 2, *D), (2, 2, *D), (3, 2, *D), (4, 2, *D),
    (3, 3, *O), (2, 3, *O),
    (1, 4, *O),
]


def get_icon(weather_code: int) -> list[tuple]:
    if weather_code == 0:
        return _SUN
    if weather_code <= 2:
        return _PARTLY_CLOUDY
    if weather_code == 3:
        return _CLOUDY
    if weather_code in (45, 48):
        return _FOG
    if weather_code in range(51, 68):
        return _RAIN
    if weather_code in range(71, 78) or weather_code in (85, 86):
        return _SNOW
    if weather_code in range(80, 83):
        return _RAIN
    if weather_code >= 95:
        return _THUNDERSTORM
    return _CLOUDY
