# AI Toolkit

A public, living record of my AI agent setup, written as Markdown. My website (`C:/Code/Readme/mbarnfield63.github.io`) checks this repo out at build time and renders it under `/toolkit/`. The full agreed design is in the vault plan: `C:/Code/Obsidian/Personal Projects/AI Toolkit/AI Toolkit_plan.md`. Read it before changing the structure.

## Layout

- `guide/`: the story, in reading order.
- `kit/`: one page per tool, plus `kit/README.md` as the index (grouped by type, sorted by status).
- `examples/`: worked runs. `examples/copy-me-exactly.md` is a full install log with its own format.
- `talks/`: one page per talk.
- `img/`: PNGs exported from the slide decks. Never commit a `.pptx`.
- `scripts/`: the check script and the figure export script (MIT).

## Writing rules

- First person, plain English. Apply `C:/Code/Obsidian/Notes/Writing Style.md`. No chemistry or physics jargon beyond what the MARVEL examples need.
- Every page starts with front matter: `title`, `description`, `order`.
- Links between pages are plain relative paths (`../kit/rtk.md`, `../img/vault.png`), so the repo reads correctly on GitHub. The website rewrites them.
- Real files (CLAUDE.md, SKILL.md, folder trees) go in as code blocks, not screenshots.
- Kit status is one of: `always-on`, `daily`, `weekly`, `occasional`, `retired`. Never delete a retired tool's page; mark it retired and say why.

## Scrub rules (public repo)

Never commit: IP addresses or home-server host details, collaborators' names, student data, email addresses, licence keys or tokens, private repo contents beyond short excerpts, or personal life admin. Run the check script before every push.

## Operating Rules

### 1. Initialize
When the user says **"get up to speed"**, invoke the `get-up-to-speed` skill. It reads the Obsidian state file at:
`C:/Code/Obsidian/Personal Projects/AI Toolkit/AI Toolkit_state.md` to reconstruct full context.

### 2. Log & Save
When reaching a milestone or when the user says **"save state"**, invoke the `save-state` skill. It:
1. Overwrites the state file (`C:/Code/Obsidian/Personal Projects/AI Toolkit/AI Toolkit_state.md`) with a clean update (see Rule 3 format).
2. Appends a summary of work done to the log file (`C:/Code/Obsidian/Personal Projects/AI Toolkit/AI Toolkit Log.md`).
3. Updates the plan (`C:/Code/Obsidian/Personal Projects/AI Toolkit/AI Toolkit_plan.md`) when a decision changes, so it never lags the state file.

Never change any other files within `C:/Code/Obsidian/`.

### 3. Obsidian State File Format
When writing to the state file, always overwrite with:

```
# AI Toolkit — Claude State

**Last Modified:** YYYY-MM-DD HH:MM

**Current Status:**
- One or two lines on where the project stands.

**Recent Wins:**
- What's been built/decided since the last save.

**Next Steps / Blockers:**
- What to pick up next session, and anything blocking it.
```
