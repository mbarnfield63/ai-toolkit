---
title: caveman
description: A plugin that makes the agent's chat replies terse, so I read less and pay for fewer output tokens.
order: 2
---

# caveman

Plugin by Julius Brussee. Status: `always-on`.
Source: [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman).

## What it is

A style rule for the agent's replies in chat. It drops filler, pleasantries, hedging and most articles, and answers in short fragments. Code, commands, file paths and error messages stay exact. A typical reply looks like this:

```
Bug in auth middleware. Token expiry check use `<` not `<=`. Fix:
```

It only changes how the agent talks to me. Anything that persists is still written in normal prose: commit messages, code comments, docs, and the pages in this repo.

## Why I use it

Most of what I read from an agent is a status line or a short answer. Without caveman, each one comes wrapped in an opening sentence and a recap. With it, the answer is the first thing on the screen, and output tokens drop as well. When something is risky, like a command that deletes data, the plugin switches back to full sentences for the warning.

## How I set it up

It is a Claude Code plugin:

```
/plugin marketplace add JuliusBrussee/caveman
/plugin install caveman@caveman
```

Hooks load it at every session start and remind the agent on every prompt, so it doesn't drift back to long replies in a long session. `/caveman lite` or `/caveman off` changes the level for one session.
