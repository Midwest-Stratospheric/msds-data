# MSDS-Data Health Alert — 2026-09-26

Generated: `2026-09-26T16:03:04Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-09-26.json (and no acceptable yesterday)

## Recent files
2026-09-19, 2026-09-20, 2026-09-21, 2026-09-22, 2026-09-23, 2026-09-24, 2026-09-25

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

