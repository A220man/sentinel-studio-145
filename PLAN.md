# Product development plan

Each round completes one feature or repair. Future items are planned, not implemented claims.

## Current round

compact-memory-skill

## Roadmap

### compact-memory-skill — Compact Memory Skill Implementation

Status: done

Acceptance:
- Skill converts prose notes to compact symbolic notation, one fact per line with consistent operators
- Skill is self-contained with SKILL.md describing the notation and write discipline
- Skill can be invoked via FastAPI endpoint /skill

Implementation: `skills/compact-memory/SKILL.md`, `skills/compact-memory/compact_memory.py`, `app.py`

Tests: `test_compact_memory.py`

