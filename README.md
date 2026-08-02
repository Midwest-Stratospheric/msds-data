# MSDS Open Data

Public atmospheric and stratospheric data releases from **Midwest Stratospheric Data Systems** high-altitude balloon flights.

## Purpose

Rapid public release (<48 hours when possible) of high-quality near-space and mid-tropospheric observations to support:

- Open science and citizen science
- Severe weather and tornado research
- Environmental monitoring
- Educational use

## Expected Data Types

- Temperature, humidity, and pressure profiles
- Wind speed/direction profiles
- GPS tracks and ascent/descent rates
- Imagery metadata and selected processed images
- Telemetry logs (APRS, WSPR, etc.)
- Flight summary reports

## Repository Structure (planned)

```
/flights/
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

Data is intended for open use with attribution to Midwest Stratospheric Data Systems. Specific licenses will be noted per release.

---

**Midwest Stratospheric Data Systems**  
Casey, Illinois | NASA GLOBE registered  
[midwestsds.com](https://www.midwestsds.com)
