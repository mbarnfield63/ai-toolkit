---
title: get-up-to-speed
description: My skill that reads a project's state file at the start of a session and briefs me on where we left off.
order: 4
---

# get-up-to-speed

Skill, written by me. Status: `daily`.

Source: [mbarnfield63/claude-state-skills](https://github.com/mbarnfield63/claude-state-skills).

## What it is

The first thing I type in almost every session. The skill finds the project's `CLAUDE.md`, reads the path of the state file from its "Initialize" rule, reads that file from my vault, and gives me a short briefing: current status, recent wins, next steps and blockers. If another agent has left ideas in a "Pending Ideas" section of the state file, it shows those too.

It is read-only. It never edits the state file, the log or the project.

## Why I use it

Every session starts with no memory. Before this skill, I pasted the same context into each new chat, or the agent spent the first few minutes reading files to work out where things stood. Now one command gets it there, and the briefing is also a check for me that the last [save-state](save-state.md) wrote what I expected.

It doesn't read the project's log at the start. The log grows without limit, and the state file already holds what the next session needs.

I used it about a hundred times in my first two months with it, which is more than any other command except `/clear`.

## How I set it up

```bash
npx skills add mbarnfield63/claude-state-skills
```

That installs both this skill and save-state into `~/.claude/skills/`, so every project can use them. Each project then needs a state file and a log in the vault, and three short rules in its `CLAUDE.md` that point at them. The repo's `templates/` folder has both.

The [CLAUDE.md and skills](../guide/02-claude-md-and-skills.md#skillmd-a-recipe-loaded-when-needed) page shows the `SKILL.md`, and [vault memory](../guide/03-vault-memory.md) explains the state file and log.
