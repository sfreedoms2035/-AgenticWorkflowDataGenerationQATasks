# Skill: QATaskGenerator

**Purpose:** Executes the primary extraction engine generating deep strategic Q&A tasks from engineering or regulatory PDFs.

**Core Capabilities:**
1. Emulates absolute expert personas (e.g., Integration Architect, Regulatory Lead).
2. Generates an exclusive 8-step internal monologue prior to formulating resolution strategy.
3. Completely avoids breaking the 'fourth wall' (Anti-Meta Rule).

**Implementation Link:**
- Main driver logic inside `run_gemini_playwright_v2.py`.
- Prompt construction within `pipeline.py`.
