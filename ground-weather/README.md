# Midwest Stratospheric Data Systems Ground Weather Data

Daily surface (ground-level) weather observations for **Casey, Illinois** — the home base of Midwest Stratospheric Data Systems.

These records provide continuous local meteorological context that complements high-altitude balloon flight profiles released in this repository.

## Location

- **Site**: Casey, IL (Clark / Cumberland County)
- **Coordinates**: 39.2992° N, 87.9925° W
- **Elevation**: ~200 m (657 ft)
- **Timezone**: America/Chicago

## Data Source

- **Provider**: [Open-Meteo](https://open-meteo.com/) (free, no API key, CC BY 4.0)
- **Models**: Best-match high-resolution numerical weather prediction (primarily NOAA GFS / HRRR and regional models)
- **Update frequency**: Daily automated collection of current conditions + daily summary

## File Structure

```
ground-weather/
├── README.md
└── daily/
    ├── YYYY-MM-DD.json   # One file per calendar day
    └── ...
```

Each daily JSON contains:

- Metadata identifying the dataset as **Midwest Stratospheric Data Systems Ground Weather Data**
- Current conditions at collection time (temperature, humidity, pressure, wind, precipitation, weather code)
- Daily aggregates for that day (max/min temperature, precipitation totals, peak winds, etc.)

Units are US customary (fahrenheit, mph, inches) for local usability.

## Attribution

Weather data © Open-Meteo. Please attribute Open-Meteo when using the raw meteorological values.

Dataset compilation and daily archival by **Midwest Stratospheric Data Systems**, Casey, Illinois.

## License

Open for research, education, and public use with attribution to Midwest Stratospheric Data Systems and Open-Meteo.

---

**Midwest Stratospheric Data Systems**  
Casey, Illinois | [midwestsds.com](https://www.midwestsds.com)
