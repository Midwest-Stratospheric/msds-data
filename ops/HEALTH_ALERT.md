# MSDS-Data Health Alert — 2026-10-03

Generated: `2026-10-03T15:58:04Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-10-03.json (and no acceptable yesterday)

## Recent files
2026-09-26, 2026-09-27, 2026-09-28, 2026-09-29, 2026-09-30, 2026-10-01, 2026-10-02

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

