# TrustCheck — Adaptive AI Study Assistant

**Prose word count: 471**

## Project status

Version 1.0 is a browser prototype for introductory Python collections. Six pre-authored AI responses (three correct and three incorrect) simulate fallible generation. The verification panel, judgement and confidence capture, deterministic adaptive suggestions, corrective feedback, session summary, export and reset are implemented. Verification examples are not executed inside the browser. Records are held in page memory and disappear on reload unless exported. Live LLM generation, retrieval and formal user evaluation are not implemented. The summary describes behaviour; it is not a validated trust-calibration score.

## Technology stack

HTML, CSS and vanilla JavaScript provide the interface. `questions.js` contains the curated tasks and source links; `logic.js` implements classification and adaptation; `app.js` manages interaction and session state. No backend, account or API key is needed. Node.js runs logic tests; Python Playwright and Chromium support browser checks.

## Running or inspecting

Open `index.html` in a modern browser, keeping all files together. Alternatively, from the project directory:

```sh
python -m http.server 8000
```

Visit `http://localhost:8000`. Try accepting question 2 at 90% confidence; question 3 should offer verification assistance. Disable adaptive assistance to hide the suggestion. Use the session summary to inspect or export records.

## Development record

- Scope: narrowed the original literature-review proposal to six controlled Python tasks to isolate explanation and verification behaviour without live model variability.
- Interaction: separated simulated advice from optional verification examples and source links; added accept, reject and unsure choices with explicit confidence capture.
- Adaptation: used the preceding judgement and confidence as provisional signals. Added a reason, dismissal and global toggle to preserve control. The 75% and 40% thresholds are design choices, not empirically validated cut-offs.
- Evaluation: separated answer keys from AI advice and added descriptive counts with denominators. Added export and reset instead of persistent profiling.
- Checks: 14 Node assertions passed; all six code examples were checked using Python. The browser check passed using an inline assembly of the same HTML, CSS and JavaScript because direct navigation was blocked in the development environment. No participant study was conducted. The documentation pages were subsequently inspected during report preparation; the student should still verify the linked sections and reproduce the checks.

```sh
node tests/logic.test.js
python tests/browser_check.py
```

The browser check requires Python Playwright and Chromium at `/usr/bin/chromium` (adjust the path for other installations).

## AI assistance

ChatGPT helped propose the scope, draft the interface, rule logic, tests, README, architecture diagram and storyboards. 
## Additional files

`docs/` contains screenshots from the automated browser walkthrough, the system architecture diagram and three screenshot-based storyboards. `tests/` contains repeatable checks. The report is submitted separately. No additional ZIP is needed once these project files are uploaded to the public repository.
