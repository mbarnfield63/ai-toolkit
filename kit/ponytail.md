---
title: ponytail
description: A plugin that makes the agent write the least code that works. Its rules load at every session start.
order: 1
---

# ponytail

Plugin by Dietrich Gebert. Status: `always-on`.

Source: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail).

## What it is

A rule set that pushes the agent towards the smallest change that works. Before it writes anything, the agent climbs a ladder and stops at the first rung that holds:

1. Does this need to exist at all?
2. Is it already in this codebase?
3. Does the standard library do it?
4. Does a native platform feature cover it?
5. Does a dependency I already have solve it?
6. Can it be one line?
7. Only then, the minimum code that works.

When the agent cuts a corner on purpose, it leaves a one-line `ponytail:` comment in the code that names the limit and the upgrade path, instead of a paragraph defending it.

## Why I use it

The usual failure of a coding agent isn't wrong code. It is too much code: a helper class nobody asked for, a config option for a value that never changes, a new dependency for something three lines would do. Research code has to be read and checked by me, so every extra line costs me time. With ponytail on, the diffs I review are shorter and the explanations after them are too.

## How I set it up

It is a Claude Code plugin. In a session:

```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

The plugin has a session-start hook, so the rules load on every start, resume and `/clear` without me asking. It also adds a few commands I use now and then: `/ponytail-review` checks a diff for over-building, `/ponytail-audit` does the same for a whole repo, and `/ponytail-debt` lists every `ponytail:` comment so the deliberate shortcuts don't get forgotten.

The [CLAUDE.md and skills](../guide/02-claude-md-and-skills.md#hooks) page explains how hooks differ from skills.
