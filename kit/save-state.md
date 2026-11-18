---
title: save-state
description: My skill that rewrites a project's state file, appends to its log, then commits and pushes just those files in my vault.
order: 5
---

# save-state

Skill, written by me. Status: `daily`.

Source: [mbarnfield63/claude-state-skills](https://github.com/mbarnfield63/claude-state-skills).

## What it is

The counterpart to [get-up-to-speed](get-up-to-speed.md). When I say "save state", the skill:

1. Finds the project's `CLAUDE.md` and reads the paths of the state file, the log and any plan document from its "Log & Save" rule.
2. Overwrites the state file with a fresh snapshot: status, recent wins, next steps.
3. Appends a dated entry to the log.
4. Updates the plan only if a decision changed.
5. Commits and pushes exactly those files in the vault repo, and nothing else.

## Why I use it

It is how a session ends, and often how one pauses. When Claude warns me that the context is filling up, I save state, `/clear`, and get up to speed again. The new session starts with a short, current summary instead of a compressed version of a long chat.

A few rules in the skill came from things going wrong:

- The state file is capped at about 8 KB. Without the cap, state files grew to 40 KB and every session start paid for them.
- Recent wins keep only the last five items. Older ones are already in the log.
- The log is appended with a shell heredoc. The agent never reads the whole log to add to it, because a long log costs a lot of tokens.
- It never runs git in the project's own repo, only in the vault.

## How I set it up

It installs with get-up-to-speed (see that page). The commit and push run without a permission prompt, because my `~/.claude/settings.json` allows exactly those git commands in the vault and nothing wider:

```json
"permissions": {
  "allow": [
    "Bash(git -C /mnt/c/Code/Obsidian status:*)",
    "Bash(git -C /mnt/c/Code/Obsidian add:*)",
    "Bash(git -C /mnt/c/Code/Obsidian commit:*)",
    "Bash(git -C /mnt/c/Code/Obsidian push:*)",
    "Bash(git -C /mnt/c/Code/Obsidian diff:*)",
    "Bash(git -C /mnt/c/Code/Obsidian log:*)"
  ]
}
```

[Vault memory](../guide/03-vault-memory.md) explains why the vault is a separate git repo.
