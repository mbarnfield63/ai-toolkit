---
title: Kit
description: Every tool in my agent setup, grouped by type and sorted by how often I use it.
order: 0
---

# Kit

Everything I have installed on top of a plain Claude Code, grouped by type. Within each group, the tools I use most come first. Tools I use at least weekly have their own page. The rest get one line.

The status says how often a tool runs:

- `always-on`: runs in every session without me asking.
- `daily`: I use it on most working days.
- `weekly`: I use it most weeks.
- `occasional`: I use it now and then, for a specific job.
- `retired`: I stopped using it. The page stays, with the reason.

## Apps

| Tool | Status | What it's for |
| --- | --- | --- |
| [Claude Code](https://code.claude.com/docs) | `daily` | The agent itself, in a terminal. Every other tool here plugs into it. |
| [Obsidian](https://obsidian.md) | `daily` | My notes vault, which is also the agents' memory. See [vault memory](../guide/03-vault-memory.md). |
| [Remote Control](remote-control.md) | `daily` | Lets me message an agent running on my home server from my phone. |

## Plugins

| Tool | Status | What it's for |
| --- | --- | --- |
| [ponytail](ponytail.md) | `always-on` | Makes the agent write the least code that works. |
| [caveman](caveman.md) | `always-on` | Makes the agent's chat replies terse. |
| [mattpocock-skills](https://github.com/mattpocock/skills) | `daily` | Matt Pocock's skills, including [grilling](grilling.md) and [tdd](tdd.md). |
| [brag](https://github.com/latent-spaces/brag) | `occasional` | Turns a project website into a short launch video. |

## Hooks

| Tool | Status | What it's for |
| --- | --- | --- |
| [rtk](rtk.md) hook | `always-on` | Sends shell commands through rtk so their output comes back shorter. |
| [herdr](herdr.md) state hook | `always-on` | Tells herdr whether each agent is working, blocked or done. |
| [ponytail](ponytail.md) and [caveman](caveman.md) | `always-on` | Load their rules at every session start. |
| [graphify](graphify.md) post-commit hook | `daily` | Rebuilds a repo's knowledge graph after every commit. |

## Skills

| Tool | Status | What it's for |
| --- | --- | --- |
| [get-up-to-speed](get-up-to-speed.md) | `daily` | Mine. Briefs me from the project's state file at the start of a session. |
| [save-state](save-state.md) | `daily` | Mine. Writes the state file and log, then commits them in the vault. |
| [grilling](grilling.md) | `daily` | Interviews me about a plan until we agree on it. |
| [hypatia](hypatia.md) | `weekly` | Mine, private. Sends GPU jobs to my department's cluster and checks on them. |
| MARVEL skills | `weekly` | Mine, private, one set per project: `marvel-lit-review`, `marvel-pipeline`, `marvel-network`, `marvel-greedy-triage`, `new-marvel-paper`, `student-handoff`. The stages of the pipeline in [multi-agent](../guide/05-multi-agent.md). |
| [tdd](tdd.md) | `occasional` | Test-first development, so the agent has a test to pass. |
| `tikz-figures` | `occasional` | Mine, private. Draws TikZ figures for papers and my thesis in my house style. |
| `diagnosing-bugs`, `codebase-design`, `domain-modeling` | `occasional` | From Matt Pocock's plugin. A loop for hard bugs, and help with code structure and naming. |
| `to-prd`, `to-issues`, `writing-great-skills` | `occasional` | Turn a conversation into a spec or a set of issues, and a reference for writing skills. |
| `find-skills` | `occasional` | Searches for an installable skill that fits a job. |
| `socratic-tutor` | `occasional` | Teaches a topic by questions, with a test at the end. |
| [HyperFrames](https://hyperframes.dev) skills | `occasional` | Make videos from HTML: `hyperframes`, `hyperframes-core`, `hyperframes-cli`, `hyperframes-animation`, `hyperframes-audio`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-registry`, `hyperframes-studio`, `general-video`, `motion-graphics`, `faceless-explainer`, `slideshow`, `pr-to-video`, `product-launch-video`, `music-to-video`, `talking-head-recut`, `embedded-captions`, `media-use`, `figma`, `remotion-to-hyperframes`. |

## Command-line tools

| Tool | Status | What it's for |
| --- | --- | --- |
| [rtk](rtk.md) | `always-on` | Shortens shell output before the agent reads it. |
| [herdr](herdr.md) | `daily` | One workspace per project, and a sidebar showing which agent needs me. |
| [graphify](graphify.md) | `daily` | Turns a codebase into a knowledge graph the agent can query. |

## MCP servers

| Tool | Status | What it's for |
| --- | --- | --- |
| [chrome-devtools](https://github.com/ChromeDevTools/chrome-devtools-mcp) | `occasional` | Lets the agent open and inspect pages in Chrome, mostly to check my website. |
