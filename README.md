# Teaching dashboard 2027

Static dashboard: one tab per class (week rows, 3 lesson cards each) plus a Schedule tab.

- `index.html`: the dashboard
- `classes/<class>.json`: lesson data per class
- `tools/`: scripts that built `physics-11.json` from the Pearson Heinemann Physics 11 sample teaching plans

Tick-offs and notes currently save in the browser (localStorage).

## 12 General Maths
- `classes/general-maths-12.json`: Unit 3 lesson order (names only so far), built by `tools/gm12/build_plan.py` from the VCE Mathematics Study Design 2023–2027 and the Cambridge General Mathematics Units 3&4 curriculum grid and sample planner.
- `index.html` reads optional fields (`unitLabel`, `summary`, `weekLabel`, `termLabel`, `assessment.rulesTitle`) so classes can use term weeks and step-up weeks. Physics does not use them and renders as before.
