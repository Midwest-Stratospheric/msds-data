# MSDS-Data Health Alert — 2026-10-23

Generated: `2026-10-23T16:43:50Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-10-23.json (and no acceptable yesterday)

## Recent files
2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-22

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

