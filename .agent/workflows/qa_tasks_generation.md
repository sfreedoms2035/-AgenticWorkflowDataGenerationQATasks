# Q&A Task Generation Workflow

This workflow drives the iterative generation of 16 deeply technical Q&A tasks per PDF document.
It leverages the Gemini model through a browser-based Playwright driver to navigate rigorous anti-regression checks.

## Flow:
1. **Document Classification Phase**: 
   - Uses `pipeline.py` to classify PDF as `TECHNICAL` or `REGULATORY`.
2. **Generation Phase (QATaskGenerator)**:
   - Evaluates the current task iteration.
   - Passes the `Q&As_V1.2.md` instruction schema and current task's variation data to the generator component.
3. **Validation & Assessment Phase (DataQualityChecker)**:
   - JSON format check.
   - Stringency verification (CoT > 10000, Content > 5000 characters).
   - Entropy check against generic filler or "keyword salad".
4. **Repair Engine Intervention (QATaskRepairer)**:
   - Applies local JSON text merging or structural string-replace fixes natively.
   - If unrepairable locally, redirects for full re-prompt with targeted error history.
5. **Preview Rendering (DataGenerationVisualizer)**:
   - Upon success, if `--preview` is enabled, `.agent/scripts/render_preview.py` transforms the JSON representation into a beautiful HTML summary and triggers the browser for manual quality review.
