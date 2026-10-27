# MSDS-Data Health Alert — 2026-10-27

Generated: `2026-10-27T17:43:01Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-10-27.json (and no acceptable yesterday)

## Recent files
2026-10-20, 2026-10-21, 2026-10-22, 2026-10-23, 2026-10-24, 2026-10-25, 2026-10-26

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

