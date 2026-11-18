---
title: graphify
description: Turns a codebase into a knowledge graph the agent can query, and a git hook keeps the graph up to date after every commit.
order: 7
---

# graphify

Command-line tool, skill and git hook. Status: `daily` (the hook runs on every commit).

Source: [graphifyy on PyPI](https://pypi.org/project/graphifyy/).

## What it is

graphify reads a folder of code (and docs, papers or images if you ask it to) and builds a knowledge graph: what each file defines, what calls what, and which parts cluster together. It writes the result to `graphify-out/`, with a plain-language report, a JSON graph and an HTML view. The agent can then ask the graph questions instead of searching file by file.

## Why I use it

On a large or unfamiliar repo, an agent's first move is to grep around until it finds its bearings. That is slow, it fills the context with file contents, and it sometimes lands in the wrong place. With a graph already built, the agent asks something like "what reads the energy levels file?" and gets a short answer that points at the right code.

I rarely run `/graphify` by hand. The work is done by the hook, which rebuilds the graph from the code after each commit, with no model calls, so the graph doesn't drift away from the code.

## How I set it up

```bash
pip install graphifyy
graphify install
```

The package is `graphifyy` with two y's. The command is `graphify`. `graphify install` adds the `/graphify` skill to Claude Code.

Then, once in each repo where I want it:

```bash
graphify hook install
```

That adds a git `post-commit` hook. I have it in my four MARVEL and ExoMol repos.

graphify is installed on the Windows side of my machine. In WSL, `~/.local/bin/graphify` is a two-line wrapper that calls the Windows executable, so one install serves both.
