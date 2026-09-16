# Midwest Stratospheric Data Systems Ground Weather Data

Daily surface (ground-level) weather observations for **Casey, Illinois** — the home base of Midwest Stratospheric Data Systems / Aerostratospheric.

These records provide continuous local meteorological context that complements high-altitude balloon flight profiles released in this repository.

## Location

- **Site**: Casey, IL (Clark / Cumberland County)
- **Coordinates**: 39.2992° N, 87.9925° W
- **Elevation**: ~200 m (657 ft)
- **Timezone**: America/Chicago

## Data Source

- **Meteorology**: [Open-Meteo](https://open-meteo.com/) (free, no API key, CC BY 4.0)
- **Radiation**: co-located GQ GMC-800 fixed station, published as a UOGW layer  
  [`layers/ground/casey/gmc-800/latest.json`](https://github.com/Midwest-Stratospheric/Unified-Open-Global-Weather/blob/main/layers/ground/casey/gmc-800/latest.json)
- **Visual desk**: [xDataHub](https://www.midwestsds.com/msds-data-hub.html)
- **Update frequency**: Daily automated collection of current conditions + daily summary + attached radiation stats when the UOGW product is present

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
- **`radiation`** — UOGW GMC-800 summary (CPM / µSv/h mean-min-max, window, observation count). Credit UOGW.

Units are US customary (fahrenheit, mph, inches) for meteorology. Radiation stays in CPM and µSv/h.

## Attribution

Weather data © Open-Meteo. Please attribute Open-Meteo when using the raw meteorological values.

Radiation layer © Aerostratospheric / UOGW. Instrument: GQ Electronics GMC-800. Credit **Unified Open Global Weather (UOGW)** and link [xDataHub](https://www.midwestsds.com/msds-data-hub.html) when reusing the radiation block.

Dataset compilation and daily archival by **Midwest Stratospheric Data Systems**, Casey, Illinois.

## License

Open for research, education, and public use with attribution to Midwest Stratospheric Data Systems, Open-Meteo, and UOGW.

---

**Midwest Stratospheric Data Systems**  
Casey, Illinois | [midwestsds.com](https://www.midwestsds.com)
