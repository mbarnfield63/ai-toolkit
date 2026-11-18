---
title: Working with agents (LLM Discussion Series, November 2026)
description: "A ten-minute talk for the agentic workflows breakout: the vault as shared memory, the MARVEL orchestrator, the cockpit, and what went wrong."
order: 2
---

# Working with agents

**Date:** 17 November 2026. **Event:** LLM Discussion Series, session 3, breakout on agentic workflows and multi-agent architectures, UCL Physics & Astronomy. **Audience:** the advanced and intermediate rooms combined: astronomy researchers from those starting out with agents to those who already write their own skills. **Length:** about ten minutes, then discussion.

Subtitle: "A PhD pipeline, a personal vault, and (too much) Claude."

## What it covered

The MARVEL pipeline carried the talk. Each slide showed one pattern, in the order the guide now follows.

| Slide | Topic | Guide page | Figure |
| --- | --- | --- | --- |
| 2 | What I mean by "agent": chat, one agent, many agents | [CLAUDE.md and skills](../guide/02-claude-md-and-skills.md) | |
| 3–4 | CLAUDE.md as the agent's job description | [CLAUDE.md and skills](../guide/02-claude-md-and-skills.md) | |
| 5 | SKILL.md: a recipe loaded only when needed | [CLAUDE.md and skills](../guide/02-claude-md-and-skills.md) | [skills.png](../img/skills.png) |
| 6 | The full kit | [kit](../kit/README.md) | |
| 7 | The deck's own brief came out of a grilling session | [a normal day](../guide/04-daily-workflow.md) | |
| 8 | The example problem: MARVEL | [many agents on one project](../guide/05-multi-agent.md) | [marvel.png](../img/marvel.png) |
| 9 | One vault, every agent | [vault memory](../guide/03-vault-memory.md) | [vault.png](../img/vault.png) |
| 10 | How work moves between me and my agents | [a normal day](../guide/04-daily-workflow.md) | [hub.png](../img/hub.png) |
| 11 | One orchestrator, many workers | [many agents on one project](../guide/05-multi-agent.md) | [orchestrator.png](../img/orchestrator.png) |
| 12 | Watching many agents at once | [the cockpit](../guide/06-cockpit.md) | [herdr.png](../img/herdr.png) |
| 13 | What's gone wrong, and discussion | | |

## What went wrong (slide 13)

- Agents paraphrased rules when passing them to each other, and the meaning drifted.
- 315 of 407 rejections an agent had approved turned out to be false.
- An agent pushed without asking.
- A train/test leak in a model evaluation.

The discussion questions: where does human sign-off go, how do you check an agent stayed in scope, when is multi-agent worth it, and what about workflows across models (Claude with Codex, for example)?

## Corrections since

Slide 8 said one wrong number "corrupts" the network. It doesn't: a wrong value makes the fit throw an error, which is what lets agents check their own work. [Many agents on one project](../guide/05-multi-agent.md) has the correct version.
