# headers-for-ExoMol

## Project Purpose

ExoMol's canonical `.states`/`.trans` files carry no in-file column headers — column meaning lives only in the `.def` file, which most users never parse by hand. This tool derives labelled headers from `.def` (or the newer `.def.json`) and offers them back as a sidecar, an inspected schema, a converted CSV, or a headered copy — without changing ExoMol's original files.

Standalone repo, MIT licence, independent of any other project, structured so it could later be donated to `github.com/exomol` if it proves useful.

**Full design decisions, rationale, and what's actually been verified against real data live in [`DESIGN.md`](DESIGN.md) — read it before making architectural changes.** It documents places where the shipped code intentionally diverges from the original plan (e.g. `.def` is JSON now, not text; whitespace-split parsing instead of fixed-width) — treat it as the source of truth over memory of earlier discussion.

## Operating Rules

### 1. Initialize
When the user says **"get up to speed"**, invoke the `get-up-to-speed` skill. It reads the Obsidian state file at:
`C:/Code/Obsidian/PhD/ExoMol Headers/ExoMol Headers_state.md` to reconstruct context.

### 2. Log & Save
When reaching a milestone or when the user says **"save state"**, invoke the `save-state` skill. It does all three:
1. Overwrite the Obsidian state file (`C:/Code/Obsidian/PhD/ExoMol Headers/ExoMol Headers_state.md`) with a clean update (see Rule 3 format).
2. Append a summary of work done to the log file (`C:/Code/Obsidian/PhD/ExoMol Headers/ExoMol Headers Log.md`).
3. Update `DESIGN.md` as necessary — new decisions as additions to the relevant section, the Testing section as new real data gets validated, and the Open/Deferred list — so the design doc never lags the state file.

Never change any other files within `C:/Code/Obsidian/`.

Note: the Obsidian note title (`ExoMol Headers`) differs from both the repo/PyPI name (`headers-for-ExoMol`) and the CLI command (`exomol-headers`) — deliberate, each name serves its own context (vault convention vs. package branding vs. typing ergonomics), not a drift bug.

### 3. Obsidian State File Format
When writing to `C:/Code/Obsidian/PhD/ExoMol Headers/ExoMol Headers_state.md`, always overwrite with:

```
# ExoMol Headers — Claude State

**Last Modified:** YYYY-MM-DD HH:MM

**Completed:**
- What's been built/validated since the last state save.

**Key decisions:**
- Anything decided this session that isn't already in DESIGN.md.

**Next Steps / Blockers:**
- Exactly what needs to be tackled next session, or what's blocking progress.
```

## Directory Structure

```
headers-for-ExoMol\      (local folder currently still named ExoMol_headers)
├── src\exomol_headers\
│   ├── def_parser.py    # .def/.def.json parsing — self-contained, never touches .states/.trans
│   ├── io_utils.py       # transparent gz/bz2 I/O, column sniffing
│   └── cli.py             # inspect / sidecar / convert / inject subcommands
├── tests\
│   └── test_def_parser.py    # assert-based, run directly or via pytest — runs against ./data, skips if absent
├── data\                  # real downloaded ExoMol datasets (gitignored — see Data Sources)
├── DESIGN.md              # full design record, decisions, and what's verified against real data
├── README.md              # user-facing usage
├── pyproject.toml         # stdlib-only core; polars/pyarrow are declared extras, not yet wired up
└── CLAUDE.md               # this file — never gitignored, never committed
```

## Data Sources

Real fixtures for end-to-end testing, kept in `./data` (gitignored, not committed — large third-party binary downloads):
- **CO** (`12C-16O__4thplus`) — diatomic, from exomol.com. 11,264 states, 609,470 transitions, single `.trans` file (4 columns, includes wavenumber).
- **H2S** (`1H2-32S__AYT2`) — triatomic, C2v, from exomol.com. 220,630 states; 115M transitions split across 35 chunk files — only chunk `00000-01000` downloaded (3 columns, no wavenumber).

Both already use the current `.def.json` format. Legacy text-`.def` support was dropped (2026-09-18) — the whole ExoMol database has migrated, so the tool only parses `.def.json` now.

## Design Constraint

`.def`/`.def.json` is a hint; the file on disk is ground truth. Never hard-fail on a mismatch between what `.def` declares and what a `.states`/`.trans` file actually contains — warn and fall back to generic column names for the unexplained part. Never mutate an original ExoMol file: `inject` always writes a copy. This is the load-bearing principle across the whole tool (see DESIGN.md's Cross-validation and Output modes sections) — any new feature that would silently trust `.def` over the actual file, or that would touch an original file in place, needs to justify breaking it, not the other way round.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
