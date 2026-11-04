# MSDS-Data Health Alert — 2026-11-04

Generated: `2026-11-04T19:31:52Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-11-04.json (and no acceptable yesterday)

## Recent files
2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31, 2026-11-01, 2026-11-02, 2026-11-03

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

