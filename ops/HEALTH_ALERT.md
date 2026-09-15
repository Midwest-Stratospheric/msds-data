# MSDS-Data Health Alert — 2026-09-15

Generated: `2026-09-15T16:34:53Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-09-15.json (and no acceptable yesterday)

## Recent files
2026-09-08, 2026-09-09, 2026-09-10, 2026-09-11, 2026-09-12, 2026-09-13, 2026-09-14

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

