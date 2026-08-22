# MSDS-Data Health Alert — 2026-08-22

Generated: `2026-08-22T19:03:21Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-08-22.json (and no acceptable yesterday)

## Recent files
2026-08-15, 2026-08-16, 2026-08-17, 2026-08-18, 2026-08-19, 2026-08-20, 2026-08-21

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

