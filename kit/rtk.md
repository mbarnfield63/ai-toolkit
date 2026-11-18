---
title: rtk
description: A command-line proxy that shortens shell output before the agent reads it.
order: 3
---

# rtk

Command-line tool and hook. Status: `always-on`.
Source: [rtk-ai/rtk](https://github.com/rtk-ai/rtk).

## What it is

rtk sits between the agent and the shell. A hook rewrites common commands (`git`, `ls`, `cat`, `grep`, test runners and many more) to go through rtk, which filters, groups and trims the output before it reaches the agent's context. A `git status` with forty untracked build files comes back as one line saying how many there are.

## Why I use it

Shell output is one of the biggest costs in a long session. Most of it is noise the agent reads once and never needs again, and it fills the context window that I'd rather spend on the actual work. rtk keeps the signal and drops the rest. `rtk gain` shows how much it has saved.

Sometimes the condensed output is too short to be useful. Then the agent re-runs the command as `rtk proxy <command>`, which passes it through untouched. A short note in my global `CLAUDE.md` tells it when to do that.

## How I set it up

I installed the binary from the project's releases page, then ran `rtk init --global`. The relevant part of `~/.claude/settings.json`:

```json
"PreToolUse": [
  {
    "matcher": "Bash",
    "hooks": [
      {
        "type": "command",
        "command": "rtk hook claude"
      }
    ]
  }
]
```

My `~/.claude/CLAUDE.md` imports the note with one line, `@RTK.md`.
