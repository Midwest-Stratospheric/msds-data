# MSDS-Data Health Alert — 2026-09-19

Generated: `2026-09-19T15:37:26Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-09-19.json (and no acceptable yesterday)

## Recent files
2026-09-12, 2026-09-13, 2026-09-14, 2026-09-15, 2026-09-16, 2026-09-17, 2026-09-18

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

