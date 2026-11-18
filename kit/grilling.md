---
title: grilling
description: Matt Pocock's skill that interviews me about a plan, with a recommended answer for every question, until we agree on it.
order: 8
---

# grilling

Skill, from Matt Pocock's skills plugin. Status: `daily`.

Source: [mattpocock/skills](https://github.com/mattpocock/skills).

## What it is

Before any code is written, the agent interviews me about what I want. It maps the plan as a tree of decisions and asks about the ones it can settle now, each with its own recommended answer. I accept, change or argue, and it moves on to the decisions that depended on those. It stops when we share an understanding of the whole plan.

Earlier versions asked one question at a time. The version I have now asks a numbered round of questions together, worded so that "yes" accepts the recommendation.

## Why I use it

My first description of a task is usually vague. If the agent starts coding from it, it guesses, and I find the wrong guesses later, in the code. Grilling moves those guesses to the start, where they cost a sentence each to fix. The recommended answers matter too. Most of the time the recommendation is right and I just say yes, so a long grilling session goes faster than it sounds.

I ran around forty grilling sessions in my first two months with it. This repo was planned in one: the layout, the build order and the scrub list were agreed before any page was written. The [normal day](../guide/04-daily-workflow.md#inside-step-2) page shows where it fits.

## How I set it up

The skills come as one Claude Code plugin:

```
/plugin marketplace add mattpocock/skills
/plugin install mattpocock-skills@mattpocock
```

Then `/grilling`, followed by what I want to make or fix, in as much detail as I can manage.
