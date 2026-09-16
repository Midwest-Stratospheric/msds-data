#!/usr/bin/env python3
"""
Fetch daily ground-level weather for Casey, IL and write Midwest Stratospheric
Data Systems Ground Weather Data JSON for the msds-data repository.

Also attaches the co-located GMC-800 ionizing-radiation layer from UOGW
(layers/ground/casey/gmc-800/latest.json) when that product is available.

Designed to run under GitHub Actions (or locally) once per day.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
from urllib.request import Request, urlopen

LAT = 39.2992
LON = -87.9925
TZ_NAME = "America/Chicago"
ELEVATION_M = 200
OUTPUT_DIR = Path("ground-weather/daily")

GMC800_URL = (
    "https://raw.githubusercontent.com/Midwest-Stratospheric/"
    "Unified-Open-Global-Weather/main/layers/ground/casey/gmc-800/latest.json"
)

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def fetch_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "MSDS-GroundWeather/1.1"})
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def fetch_open_meteo() -> dict:
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LAT}&longitude={LON}"
        f"&current=temperature_2m,relative_humidity_2m,dew_point_2m,apparent_temperature,"
        f"precipitation,rain,weather_code,cloud_cover,pressure_msl,surface_pressure,"
        f"wind_speed_10m,wind_direction_10m,wind_gusts_10m"
        f"&daily=temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,"
        f"precipitation_sum,rain_sum,snowfall_sum,precipitation_hours,"
        f"wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant"
        f"&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch"
        f"&timezone={TZ_NAME}&forecast_days=1"
    )
    return fetch_json(url)


def radiation_block(gmc: dict | None) -> dict:
    if not gmc:
        return {
            "available": False,
            "note": "UOGW GMC-800 latest.json not reachable this run.",
        }
    stats = gmc.get("stats") or {}
    hours = gmc.get("hourly") or []
    last = hours[-1] if hours else None
    return {
        "available": True,
        "layer": "UOGW",
        "credit": "Unified Open Global Weather (UOGW)",
        "xdatahub": "https://www.midwestsds.com/msds-data-hub.html",
        "source_url": GMC800_URL,
        "station_id": (gmc.get("site") or {}).get("id", "MSDS-GMC800-CASEY"),
        "instrument": "GQ Electronics GMC-800",
        "kind": "fixed_ground_station",
        "native_interval": gmc.get("native_interval", "1min"),
        "product_interval": gmc.get("product_interval", "hourly"),
        "window_start_local": gmc.get("window_start_local"),
        "window_end_local": gmc.get("window_end_local"),
        "observation_count": gmc.get("observation_count"),
        "cpm": stats.get("cpm"),
        "usv_h": stats.get("usv_h"),
        "latest_hour": last,
        "note": "Co-located Casey ionizing radiation. Research series, not a health-physics product.",
    }


def build_record(data: dict, gmc: dict | None) -> tuple[str, dict]:
    now_local = datetime.now(ZoneInfo(TZ_NAME))
    now_utc = datetime.now(timezone.utc)
    local_date = now_local.strftime("%Y-%m-%d")
    collected_local = now_local.strftime("%Y-%m-%dT%H:%M")
    collected_utc = now_utc.strftime("%Y-%m-%dT%H:%M:%SZ")

    cur = data["current"]
    daily = data["daily"]
    code = cur.get("weather_code")
    desc = WEATHER_CODES.get(code, f"Code {code}")

    record = {
        "dataset": "Midwest Stratospheric Data Systems Ground Weather Data",
        "location": {
            "name": "Casey, Illinois",
            "latitude": LAT,
            "longitude": LON,
            "elevation_m": ELEVATION_M,
            "timezone": TZ_NAME,
        },
        "source": {
            "provider": "Open-Meteo",
            "url": "https://open-meteo.com/",
            "license": "CC BY 4.0",
            "attribution": "Weather data by Open-Meteo.com",
            "radiation_layer": "UOGW Casey GMC-800",
        },
        "collection": {
            "date": local_date,
            "collected_at_local": collected_local,
            "collected_at_utc": collected_utc,
            "notes": "Automated daily ground-level observation for MSDS flight context and open data archive. Includes co-located GMC-800 radiation when UOGW latest.json is present.",
        },
        "current": {
            "time": cur["time"],
            "temperature_2m_f": round(cur["temperature_2m"], 1),
            "relative_humidity_2m_pct": cur["relative_humidity_2m"],
            "apparent_temperature_f": round(cur["apparent_temperature"], 1),
            "precipitation_in": round(cur["precipitation"], 3),
            "weather_code": code,
            "weather_description": desc,
            "pressure_msl_hpa": round(cur["pressure_msl"], 1),
            "surface_pressure_hpa": round(cur["surface_pressure"], 1),
            "wind_speed_10m_mph": round(cur["wind_speed_10m"], 1),
            "wind_direction_10m_deg": cur["wind_direction_10m"],
            "wind_gusts_10m_mph": round(cur["wind_gusts_10m"], 1),
        },
        "daily": {
            "date": daily["time"][0],
            "temperature_2m_max_f": round(daily["temperature_2m_max"][0], 1),
            "temperature_2m_min_f": round(daily["temperature_2m_min"][0], 1),
            "apparent_temperature_max_f": round(daily["apparent_temperature_max"][0], 1),
            "apparent_temperature_min_f": round(daily["apparent_temperature_min"][0], 1),
            "precipitation_sum_in": round(daily["precipitation_sum"][0], 3),
            "rain_sum_in": round(daily["rain_sum"][0], 3),
            "snowfall_sum_in": round(daily["snowfall_sum"][0], 3),
            "precipitation_hours": daily["precipitation_hours"][0],
            "wind_speed_10m_max_mph": round(daily["wind_speed_10m_max"][0], 1),
            "wind_gusts_10m_max_mph": round(daily["wind_gusts_10m_max"][0], 1),
            "wind_direction_10m_dominant_deg": daily["wind_direction_10m_dominant"][0],
        },
        "radiation": radiation_block(gmc),
        "units": {
            "temperature": "\u00b0F",
            "precipitation": "inch",
            "wind_speed": "mph",
            "pressure": "hPa",
            "humidity": "%",
            "cpm": "counts per minute",
            "usv_h": "\u00b5Sv/h",
        },
    }
    return local_date, record


def main() -> int:
    print("Fetching Open-Meteo data for Casey, IL ...")
    try:
        data = fetch_open_meteo()
    except Exception as exc:
        print(f"ERROR: failed to fetch weather data: {exc}", file=sys.stderr)
        return 1

    gmc = None
    try:
        print("Fetching UOGW GMC-800 radiation layer ...")
        gmc = fetch_json(GMC800_URL)
    except Exception as exc:
        print(f"WARN: GMC-800 layer not attached: {exc}", file=sys.stderr)

    date_str, record = build_record(data, gmc)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"{date_str}.json"

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Wrote {out_path}")
    print(f"  Temperature: {record['current']['temperature_2m_f']} \u00b0F")
    print(f"  Conditions:  {record['current']['weather_description']}")
    rad = record["radiation"]
    if rad.get("available") and rad.get("cpm"):
        print(f"  Radiation:   mean {rad['cpm'].get('mean')} CPM / {rad['usv_h'].get('mean')} uSv/h")
    else:
        print("  Radiation:   not attached")
    print(f"  Collected:   {record['collection']['collected_at_local']} local")
    return 0


if __name__ == "__main__":
    sys.exit(main())
