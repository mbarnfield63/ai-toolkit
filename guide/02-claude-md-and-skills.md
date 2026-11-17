---
title: CLAUDE.md and skills
description: The job description an agent reads every session, the recipes it loads only when needed, and where both files sit.
order: 2
---

# CLAUDE.md and skills

An agent starts every session with no memory. Two kinds of plain Markdown file tell it where it is and how to do the jobs I repeat.

## CLAUDE.md: the job description

`CLAUDE.md` sits in the project folder, and the agent reads it before it does anything else. It is written for the agent, not for people.

Here is the real one from a small tool of mine that adds column headers to ExoMol data files. I've cut the section at the end that tells the agent how to use [graphify](../kit/graphify.md).

````markdown
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
````

The top says what the project is and why it exists, in two short paragraphs. Then it points at a design document and says that document wins over anything the agent remembers. `CLAUDE.md` doesn't have to hold everything. It tells the agent where to look.

The operating rules say how a session starts and ends. "Get up to speed" reads my notes on the project, and "save state" writes them back. Those two phrases are skills, shown below, and the [vault memory](03-vault-memory.md) page explains the notes they read and write.

The second half is practical. A map of the folders, so the agent doesn't have to search for where things are. Where the real test data is, and what it looks like. And the one rule that everything else depends on: the original ExoMol files are never changed, and when the files disagree with their description, the agent warns instead of failing.

You don't need to write all this at once. In Claude Code, `/init` reads your code and drafts a first version. I add the state and log rules by hand on top, and they have the same shape in every project. After that, every time the agent makes the same mistake twice, I add one line. Other agents use the same idea under a different name, usually `AGENTS.md`.

### One per project, not one for everything

Every research project has its own conventions, environment and stage of maturity. A single `CLAUDE.md` for all of them either drowns in project-specific rules or stays too generic to help. With one per project, the agent only loads the rules for the folder it is sitting in.

## SKILL.md: a recipe loaded when needed

A skill is a recipe for a job I repeat. Each skill is a folder with one file in it, `SKILL.md`, plus any scripts it needs. Here is [get-up-to-speed](../kit/get-up-to-speed.md), the skill named in the `CLAUDE.md` above:

```markdown
---
name: get-up-to-speed
description: "Use when the user says \"get up to speed\" (or /get-up-to-speed) in any project repo. Reads that project's Obsidian state file to reconstruct full context at the start of a session."
---

# /get-up-to-speed

Reconstructs session context from a project's Obsidian state file. Works in any code project that has a `CLAUDE.md` with an "Initialize"/"get up to speed" rule pointing at a vault state file — no per-project setup needed beyond that existing convention.

## What to do when invoked

1. **Find the project's `CLAUDE.md`.** Start at the current working directory and walk upward until one is found (stop at the first one, don't keep climbing past it).

2. **Extract the state file path.** Search the CLAUDE.md content for the "Initialize" rule (heading containing "Initialize" or "get up to speed", usually `### 1. Initialize`) and pull the backtick-quoted path ending in `_state.md`. If that heading isn't found, fall back to the first backtick-quoted `*_state.md` path anywhere in the file.

3. **Read the state file.** If it doesn't exist, say so and stop — don't create one silently (that's `save-state`'s job).

4. **Also check for a `## Pending Ideas (VaultAgent)` section** in the state file — if present and non-empty, surface those items too (they were routed here by VaultAgent between sessions).

5. **Summarize, don't dump.** Present the state back as a short briefing: current status, recent wins, next steps/blockers, and any pending ideas — not a raw file cat. This is the point of the skill: turn the state file into an actual "here's where we left off" for the session.

## Notes

- Do not read the log or a linked `<Project>_reference.md` at the start. Open the reference file only when the task needs it. To search the log, use `grep -n '^## '` and read only the lines you need.
- Read-only. Never edits the state file, the log, or the project's `CLAUDE.md`.
- If the CLAUDE.md also names a plan/design doc (e.g. a `*_plan.md`) as something that shouldn't lag the state file, it's fine to skim it too if the state file references something the plan would clarify — but the state file is the primary source of truth for "where we are."
- This is the counterpart to `save-state` — always keep the two in sync in behavior (same path-discovery logic).
```

The agent always sees the `name` and `description` at the top, so it knows the skill exists and when to use it. The steps below only load when the skill runs. I can run it by name with `/get-up-to-speed`, or just say the phrase and the agent picks it from the description.

That is the difference from `CLAUDE.md`. `CLAUDE.md` is read every session, and a skill costs nothing until you need it. So `CLAUDE.md` holds the rules, and skills hold the procedures. A good first skill is whatever you explain to the agent more than twice.

## Where they sit

<!-- FIGURE: v3 slide 5, folder trees for ~/.claude and a project, "both load together" -->

Both kinds of file sit in two places. My home folder holds the ones for every project. "Get up to speed" lives there because every project uses it:

```
~/.claude/
  CLAUDE.md
  skills/get-up-to-speed/
    SKILL.md
```

A project folder holds its own, like the network skill in my MARVEL pipeline. A subfolder can add extra rules for work in that folder:

```
MARVEL_pipeline/
  CLAUDE.md
  .claude/skills/marvel-network/
    SKILL.md
  network/CLAUDE.md
```

When I start a session in a project, both sets load together.

## Hooks

Skills fire when named, or when the agent decides the description fits. Hooks fire on their own, without being asked. Two of mine:

- [ponytail](../kit/ponytail.md) loads its full rule set at every session start, so it is always on and I never invoke it per task.
- [graphify](../kit/graphify.md) checks the diff after every git commit and rebuilds the project's knowledge graph as needed, so the graph never goes stale.

The full list of what I have installed, and what each one is for, is in the [kit](../kit/README.md).
