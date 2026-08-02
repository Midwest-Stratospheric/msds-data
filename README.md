# MSDS Open Data

Public atmospheric and stratospheric data releases from **Midwest Stratospheric Data Systems** high-altitude balloon flights, plus continuous local ground weather observations.

## Purpose

Rapid public release (<48 hours when possible) of high-quality near-space and mid-tropospheric observations to support:

- Open science and citizen science
- Severe weather and tornado research
- Environmental monitoring
- Educational use

## Data Available

### Ground Weather Data (Casey, IL)
Daily surface weather observations automatically archived as **Midwest Stratospheric Data Systems Ground Weather Data**.

- Location: Casey, Illinois (home base)
- See [`ground-weather/`](ground-weather/) for daily JSON files and documentation
- Source: Open-Meteo (CC BY 4.0)

### High-Altitude Flight Data (coming)
- Temperature, humidity, and pressure profiles
- Wind speed/direction profiles
- GPS tracks and ascent/descent rates
- Imagery metadata and selected processed images
- Telemetry logs (APRS, WSPR, etc.)
- Flight summary reports

## Repository Structure

```
/ground-weather/
  README.md
  /daily/
    YYYY-MM-DD.json

/flights/   (planned)
  /YYYY-MM-DD_flight-id/
    metadata.json
    profiles/
    tracks/
    imagery/
    raw/
```

## Related Repositories

- [msds-website](https://github.com/Midwest-Stratospheric/msds-website) — Public data portal and site
- [x2griffon](https://github.com/Midwest-Stratospheric/x2griffon) — Payload platform
- [msds-docs](https://github.com/Midwest-Stratospheric/msds-docs) — Documentation and procedures

## License & Attribution

Data is intended for open use with attribution to Midwest Stratospheric Data Systems. Ground weather values should also attribute Open-Meteo. Specific licenses will be noted per release.

---

**Midwest Stratospheric Data Systems**  
Casey, Illinois | NASA GLOBE registered  
[midwestsds.com](https://www.midwestsds.com)
