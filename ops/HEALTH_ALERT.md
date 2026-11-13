# MSDS-Data Health Alert — 2026-11-13

Generated: `2026-11-13T19:23:17Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-11-13.json (and no acceptable yesterday)

## Recent files
2026-11-06, 2026-11-07, 2026-11-08, 2026-11-09, 2026-11-10, 2026-11-11, 2026-11-12

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

