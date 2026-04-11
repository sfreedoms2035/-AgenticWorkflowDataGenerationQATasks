# Agent Configuration (Q&A Tasks Pipeline)

## Environment
- **OS:** Windows 11
- **Python:** Python 3 (Anaconda)
- **Browser Automation:** Playwright

## Project Paths
- **Project Root:** `C:\Users\User\VS_Projects\Helpers\Antigravity\AgenticWorkflowPlaywright_QAs`
- **Input PDFs:** `Input/`
- **Output JSON:** `Output/json/`
- **Output Thinking:** `Output/thinking/`
- **QA & Eval:** `Eval/`
- **Scripts:** `.agent/scripts/`

## Core Pipeline Entry Point
```
python pipeline.py                    # Process all PDFs
python pipeline.py --resume           # Resume from checkpoint
python pipeline.py --preview          # Render HTML and open preview for completed tasks
```

## Scripts
| Script | Purpose |
|--------|---------|
| `validate_task.py` | Validates Q&A schema formatting, content/CoT char lengths, missing tags, and text entropy. |
| `auto_repair.py` | Local repair engine (malformed JSON arrays, markdown wrapper removal). |
| `render_preview.py`| Renders the generated JSON as stylized HTML and opens the system's browser to preview. |

## Role Variation
Follows `Q&As_Variation_V1.1.md`. Alternates Technical and Regulatory documents logic across 16 tasks.

## Quality Gates
- **CoT length:** ≥ 10,000 chars (warning if below, fail if missing)
- **Content length:** ≥ 5,000 chars 
- **Repetitive/Filler Check:** Checks for n-gram loop anomalies.
- **Conversations structure:** Exact alternating Role: User/Assistant schema.
