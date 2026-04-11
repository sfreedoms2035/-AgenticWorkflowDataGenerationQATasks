# Skill: QATaskRepairer

**Purpose:** Locally detects and patches anomalies in the generated LLM structures without requiring costly re-prompts.

**Core Capabilities:**
1. Fixes broken JSON array closures efficiently.
2. Identifies leaked reasoning tags inside content mapping.
3. Fixes merged user/assistant prompt loops.

**Implementation Link:**
- Main driver logic inside `.agent/scripts/auto_repair.py`.
