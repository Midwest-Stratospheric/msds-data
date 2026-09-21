#!/usr/bin/env python3
"""Pull Aerostratospheric Weather Underground PWS KILCASEY47 into ground-weather/wunderground/."""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

STATION = os.environ.get("WU_STATION", "KILCASEY47")
API_KEY = os.environ.get("WU_API_KEY", "").strip()
OUT_DIR = Path("ground-weather/wunderground")
TZ = ZoneInfo("America/Chicago")


def fetch_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "MSDS-GroundWeather-WU/1.0"})
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def row_from_obs(obs: dict) -> dict:
    imp = obs.get("imperial") or {}
    return {
        "time_local": obs.get("obsTimeLocal"),
        "time_utc": obs.get("obsTimeUtc"),
        "temp_f": imp.get("temp"),
        "dewpt_f": imp.get("dewpt"),
        "heat_index_f": imp.get("heatIndex"),
        "humidity_pct": obs.get("humidity"),
        "wind_mph": imp.get("windSpeed"),
        "gust_mph": imp.get("windGust"),
        "winddir_deg": obs.get("winddir"),
        "pressure_in": imp.get("pressure"),
        "precip_rate_in": imp.get("precipRate"),
        "precip_total_in": imp.get("precipTotal"),
        "uv": obs.get("uv"),
        "solar": obs.get("solarRadiation"),
    }


def main() -> int:
    if not API_KEY:
        print("ERROR: set WU_API_KEY (GitHub Actions secret).", file=sys.stderr)
        return 1
    base = "https://api.weather.com/v2/pws"
    q = f"stationId={STATION}&format=json&units=e&numericPrecision=decimal&apiKey={API_KEY}"
    current = fetch_json(f"{base}/observations/current?{q}")
    day = fetch_json(f"{base}/observations/all/1day?{q}")
    obs = (current.get("observations") or [None])[0] or {}
    imp = obs.get("imperial") or {}
    series = [row_from_obs(r) for r in (day.get("observations") or [])]
    now = datetime.now(timezone.utc)
    local = datetime.now(TZ)
    pack = {
        "dataset": "Midwest Stratospheric Data Systems Ground Weather Data",
        "layer": "ground-weather",
        "kind": "fixed_ground_station",
        "station": {
            "id": STATION,
            "network": "Weather Underground",
            "name": "Aerostratospheric",
            "neighborhood": obs.get("neighborhood"),
            "latitude": obs.get("lat"),
            "longitude": obs.get("lon"),
            "elevation_ft": imp.get("elev"),
            "dashboard": f"https://www.wunderground.com/dashboard/pws/{STATION}",
        },
        "source": {
            "provider": "Weather Underground / The Weather Company",
            "product": "PWS observations",
            "station_id": STATION,
            "attribution": f"Observations from Aerostratospheric Weather Underground station {STATION}.",
        },
        "collection": {
            "date": local.strftime("%Y-%m-%d"),
            "collected_at_local": local.strftime("%Y-%m-%dT%H:%M"),
            "collected_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        "current": row_from_obs(obs),
        "observations_1day_count": len(series),
        "observations_1day": series,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dated = OUT_DIR / f"{pack['collection']['date']}.json"
    latest = OUT_DIR / "latest.json"
    text = json.dumps(pack, indent=2) + "\n"
    dated.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    cur = pack["current"]
    print(f"Wrote {dated} and {latest}")
    print(f"  {STATION} {cur.get('temp_f')} F  RH {cur.get('humidity_pct')}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
