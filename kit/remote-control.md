---
title: Remote Control
description: A Claude Code feature that lets me use a session running on another machine from my phone. It is how I reach VaultAgent.
order: 9
---

# Remote Control

Claude Code feature. Status: `daily`.

Docs: [Remote Control](https://code.claude.com/docs/en/remote-control).

## What it is

Remote Control connects a Claude Code session running on one machine to the Claude app on another device. The session keeps running where it started, with that machine's files and tools, and I type into it from my phone or a browser.

## Why I use it

I keep one agent, VaultAgent, running all the time in my Obsidian vault on a home server. Ideas tend to arrive away from my desk. With Remote Control I message VaultAgent from my phone, and it files the idea in the right place: a project idea goes into that project's state file under "Pending Ideas", where [get-up-to-speed](get-up-to-speed.md) shows it at the start of the next session. It can also transcribe a video or summarise a GitHub link into a note for later.

Because the agent runs on the server, not on my phone, it has the whole vault and its own tools, and it carries on if my phone loses signal. The [normal day](../guide/04-daily-workflow.md) page shows where it fits.

## How I set it up

On the server, in the vault folder:

```bash
claude remote-control
```

The session then appears in the Claude app under my account. Remote Control is still a research preview, so check the docs for your plan and version before relying on it.
