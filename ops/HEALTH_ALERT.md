# MSDS-Data Health Alert — 2026-09-05

Generated: `2026-09-05T14:50:49Z`
Critical failure: **True**
Status: `missing`

## Reasons
- no ground-weather/daily/2026-09-05.json (and no acceptable yesterday)

## Recent files
2026-08-29, 2026-08-30, 2026-08-31, 2026-09-01, 2026-09-02, 2026-09-03, 2026-09-04

## Recovery

This PR is opened automatically when daily ground-weather JSON is missing or stale.
It is **closed automatically** when Health Monitor reports recovery.

1. Re-run **Daily Ground Weather (Casey IL)**
2. Or ensure UOGW `msds-ground-daily` dual-write token is valid
3. Re-run **MSDS Data Health Monitor**

