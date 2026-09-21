#!/usr/bin/env python3
"""Pull Aerostratospheric Fixed Weather Station KILCASEY47 into ground-weather/wunderground/."""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

STATION = os.environ.get("WU_STATION", "KILCASEY47")
STATION_NAME = "Aerostratospheric Fixed Weather Station KILCASEY47"
API_KEY = os.environ.get("WU_API_KEY", "").strip()
OUT_DIR = Path("ground-weather/wunderground")
TZ = ZoneInfo("America/Chicago")


def first(*vals):
    for v in vals:
        if v is not None:
            return v
    return None


def fetch_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "MSDS-GroundWeather-WU/1.0"})
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def row_from_obs(obs: dict) -> dict:
    imp = obs.get("imperial") or {}
    return {
        "time_local": obs.get("obsTimeLocal"),
        "time_utc": obs.get("obsTimeUtc"),
        "temp_f": first(imp.get("temp"), imp.get("tempAvg")),
        "dewpt_f": first(imp.get("dewpt"), imp.get("dewptAvg")),
        "heat_index_f": first(imp.get("heatIndex"), imp.get("heatindexAvg")),
        "humidity_pct": first(obs.get("humidity"), obs.get("humidityAvg")),
        "wind_mph": first(imp.get("windSpeed"), imp.get("windspeedAvg")),
        "gust_mph": first(imp.get("windGust"), imp.get("windgustHigh")),
        "winddir_deg": first(obs.get("winddir"), obs.get("winddirAvg")),
        "pressure_in": first(imp.get("pressure"), imp.get("pressureMax")),
        "precip_rate_in": imp.get("precipRate"),
        "precip_total_in": imp.get("precipTotal"),
        "uv": first(obs.get("uv"), obs.get("uvHigh")),
        "solar_wm2": first(obs.get("solarRadiation"), obs.get("solarRadiationHigh")),
        "solar": first(obs.get("solarRadiation"), obs.get("solarRadiationHigh")),
        "solar_high_wm2": obs.get("solarRadiationHigh"),
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
    day_rows = day.get("observations") or []
    last = day_rows[-1] if day_rows else {}
    imp = obs.get("imperial") or {}
    series = [row_from_obs(r) for r in day_rows]
    now = datetime.now(timezone.utc)
    local = datetime.now(TZ)
    cur = row_from_obs(obs)
    last_row = row_from_obs(last) if last else {}
    for key in list(cur.keys()):
        if cur.get(key) is None and last_row.get(key) is not None:
            cur[key] = last_row.get(key)
    pack = {
        "dataset": STATION_NAME,
        "layer": "ground-weather",
        "kind": "fixed_ground_station",
        "station": {
            "id": STATION,
            "network": "Weather Underground",
            "name": STATION_NAME,
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
            "attribution": STATION_NAME,
        },
        "collection": {
            "date": local.strftime("%Y-%m-%d"),
            "collected_at_local": local.strftime("%Y-%m-%dT%H:%M"),
            "collected_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        "current": cur,
        "observations_1day_count": len(series),
        "observations_1day": series,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dated = OUT_DIR / f"{pack['collection']['date']}.json"
    latest = OUT_DIR / "latest.json"
    text = json.dumps(pack, indent=2) + "\n"
    dated.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    print(f"Wrote {dated} and {latest}")
    print(
        f"  {STATION_NAME} {cur.get('temp_f')} F  RH {cur.get('humidity_pct')}%  solar {cur.get('solar_wm2')} W/m2"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
