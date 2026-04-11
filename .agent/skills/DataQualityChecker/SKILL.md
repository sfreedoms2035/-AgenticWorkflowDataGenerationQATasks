# Skill: DataQualityChecker

**Purpose:** Enforces an unyielding stringency parameter for validation before a generation can be marked successful and recorded.

**Core Capabilities:**
1. Verifies the JSON layout completely maps the schema required by Q&A definition.
2. Calculates and verifies textual size metrics (e.g. >10k characters internal CoT, >5000 characters resolution framework).
3. Performs an N-Gram text sequence analysis to avoid AI looping and filler keyword generation.

**Implementation Link:**
- Check criteria applied through `.agent/scripts/validate_task.py`.
