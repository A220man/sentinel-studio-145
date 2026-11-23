# Changelog

## 1.2.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.1.0 — compact-memory-skill implementation

- Implemented `compact_memory()` function in `skills/compact-memory/compact_memory.py`
  - Converts prose notes to compact symbolic notation `<TYPE>:<VALUE>`
  - Four types: `task`, `note`, `rule`, `obs`
  - Splits input on sentence boundaries (`. `) and classifies each sentence
  - Rule patterns (`=>`) are detected and classified as `task` or `rule`
- Added FastAPI `/skill` endpoint in `app.py` for skill invocation
- All 4 unit tests passing in `test_compact_memory.py`

## 1.0.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.
