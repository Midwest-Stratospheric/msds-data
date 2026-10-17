# MSDS-Data Health Alert — 2026-10-17

Generated: `2026-10-17T15:14:10Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-10-17.json (and no acceptable yesterday)

## Recent files
2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

