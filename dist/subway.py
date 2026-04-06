from __future__ import annotations

import os
import time
from dataclasses import dataclass
from datetime import datetime

os.environ.setdefault("TZ", "America/New_York")
time.tzset()

from nyct_gtfs import NYCTFeed

# --- Configuration ---
# Each entry: (stop_id, label, allowed_lines)
STATIONS = [
    ("R05S", "Bway", {"N", "W"}),      # Broadway — N/W southbound (Manhattan-bound)
    ("G19S", "Stnwy", {"R"}),           # Steinway St — R southbound (Manhattan-bound)
]
FEED_ID = "N"  # N/Q/R/W feed group (covers both stations)
MAX_DEPARTURES = 4


@dataclass
class Departure:
    line: str
    minutes: int
    destination: str
    station: str  # short label for which station


_feed: NYCTFeed | None = None


def fetch_subway() -> list[Departure] | None:
    global _feed
    try:
        if _feed is None:
            _feed = NYCTFeed(FEED_ID)
        else:
            _feed.refresh()

        stop_ids = [s[0] for s in STATIONS]
        trips = _feed.filter_trips(headed_for_stop_id=stop_ids)

        # Build lookup: stop_id -> (label, allowed_lines)
        stop_cfg = {s[0]: (s[1], s[2]) for s in STATIONS}

        now = datetime.now()  # local time (TZ=America/New_York)
        departures: list[Departure] = []

        for trip in trips:
            for stop in trip.stop_time_updates:
                if stop.stop_id in stop_cfg and stop.arrival is not None:
                    label, allowed = stop_cfg[stop.stop_id]
                    if trip.route_id not in allowed:
                        break
                    minutes = int((stop.arrival - now).total_seconds() // 60)
                    if minutes < 0:
                        break
                    dest = trip.headsign_text or ""
                    departures.append(
                        Departure(
                            line=trip.route_id,
                            minutes=minutes,
                            destination=dest,
                            station=label,
                        )
                    )
                    break

        departures.sort(key=lambda d: d.minutes)
        return departures[:MAX_DEPARTURES]

    except Exception:
        return None
