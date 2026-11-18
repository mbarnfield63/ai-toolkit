---
title: herdr
description: A terminal workspace manager for agent sessions that shows which agent is working, blocked or done.
order: 6
---

# herdr

Terminal app and hook. Status: `daily` (its state hook is `always-on`).

Source: [herdr.dev](https://herdr.dev).

## What it is

A terminal multiplexer built for running several coding agents at once. I keep one workspace per project, each with its own panes. A sidebar lists every agent session and its state: working, blocked on a question, or done.

## Why I use it

Once more than two agents are running, the hard part is knowing which one is waiting for me. Before herdr I cycled through terminal tabs to check. Now a glance at the sidebar tells me where to go. The [cockpit](../guide/06-cockpit.md) page has a screenshot.

## How I set it up

I installed it from herdr.dev. herdr installs its own Claude Code integration: a hook script at `~/.claude/hooks/herdr-agent-state.sh`, registered in `~/.claude/settings.json` to run whenever a session starts, resumes or clears:

```json
"SessionStart": [
  {
    "matcher": "^(startup|resume|clear|compact|fork)$",
    "hooks": [
      {
        "type": "command",
        "command": "bash '/home/marco/.claude/hooks/herdr-agent-state.sh' session",
        "timeout": 10
      }
    ]
  }
]
```

The script exits straight away outside herdr, so it costs nothing in a plain terminal. Inside herdr, it reports the session to the pane it runs in, which is how the sidebar knows each agent's state. herdr overwrites the script when it updates, so any extra hooks of mine go beside it, not inside it.
