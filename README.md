# AgenticWorkflowDataGenerationQATasks

Autonomous, self-healing pipeline for generating synthetic, dialectic Q&A engineering tasks using Gemini and Playwright. This pipeline extracts rigorous 8-block semantic reasoning schemas to construct high-fidelity AI training data, gracefully sidestepping native JSON generation constraints and UI extraction limitations.

## Pipeline Architecture

This repository encapsulates the complete Q&A engineering data generation logic:
1. **Orchestrator (`pipeline.py`)**: Master state machine handling job routing, retry loops, and schema assembly logic.
2. **Execution (`run_gemini_playwright_v2.py`)**: Playwright automation acting as a virtualized terminal (VT100) to force granular, plain-text semantic block output from the Gemini web application, bypassing the model's restrictive UI Canvas layer.
3. **Validation (`.agent/scripts/validate_task.py`)**: A strict quality gate verifying lengths, formatting, prompt constraint alignment, and checking for hallucinated variables.
4. **Local Repair (`.agent/scripts/auto_repair.py` & `partial_repair.py`)**: Self-healing regex algorithms that intercept and resolve structural faults (stripped markdown tags, redundant prefixes) without needing costly LLM round-trips.

## 🚀 Installation Guidelines (Fresh Machine Setup)

Follow these strict instructions to set up the pipeline on a newly provisioned computer.

### 1. Prerequisites
- **Python 3.10+**
- **Node.js**: Required to power `@llamaindex/liteparse` for caching raw text out of the source PDFs.

### 2. Prepare Environment
Open a terminal (Powershell or Bash) and clone the repository:
```sh
git clone https://github.com/sfreedoms2035/-AgenticWorkflowDataGenerationQATasks.git
cd -AgenticWorkflowDataGenerationQATasks
```

Create and activate a virtual environment:
```sh
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required python packages and the Playwright browser binaries:
```sh
pip install -r requirements.txt
playwright install
```

### 4. Provide Input Data
Create an `Input` directory in the repository root and place all structural source PDFs inside.
```sh
mkdir Input
# Copy your .pdf files into the Input/ directory
```

## 🛠️ Usage

Ensure your terminal's character encoding is set to UTF-8 to prevent extraction crashes during intense Japanese or technical mathematical symbols:
```powershell
$env:PYTHONIOENCODING="utf-8"
$env:PYTHONUNBUFFERED="1"
```

### Master CLI Options
```sh
# Start or seamlessly resume the generation array across all PDFs
python pipeline.py --resume

# Resume process and automatically open local HTML previews of successfully generated Q&A pairs
python pipeline.py --resume --preview

# STRICT UI extraction: Will fail tasks if the Gemini thinking modal cannot be parsed correctly 
# (By default this is optional to prevent false-negative pipeline blocks)
python pipeline.py --resume --strict-thinking

# Generate tasks for a specific standalone PDF
python pipeline.py --pdf "name_of_document.pdf"
```

## Track & Outputs
Outputs will be aggregated in the `/Output/json/` directory containing complete 6-turn structured JSON representations. System progression is captured iteratively inside `Output/progress.json`.
