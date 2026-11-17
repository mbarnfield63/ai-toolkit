---
title: Agents
description: What I mean by an agent, and the two ways to run more than one.
order: 1
---

# Agents

I'm a PhD student working on molecular spectroscopy for exoplanet atmospheres. Most of my work now runs through Claude Code. Before anything else, here is what I mean by "agent", because the rest of the guide uses the word a lot.

<!-- FIGURE: slide 3, three panels: chat, agent, many agents -->

## Chat

Most people start with a chat window. You paste in code or an error, it answers, and you paste the answer back. You are the one carrying information in and out.

Anyone who has had a long back-and-forth with a chatbot has hit the same wall. It starts going in circles, suggests things you already ruled out, and forgets what you told it three messages ago. Eventually the conversation is more work to steer than to restart. The cause is the context window: a long session gets worse well before the hard limit, because the useful information is buried under everything else that has been said. Most of my setup exists to manage what is in that window.

## An agent

An agent is the same model with tools, working in a loop. It reads files, runs commands, edits code and checks the result itself, until the job is done. Claude Code is one.

An agent starts in a folder, and that folder's `CLAUDE.md` is its job description: what the project is, the rules, and where its notes live. The [next page](02-claude-md-and-skills.md) shows a real one.

## Many agents

You can have more than one agent in two ways.

**Subagents.** A running session spawns them for a task, like "judge this batch of papers". Each one gets a fresh context, does its task and reports back a summary. Subagents can't spawn their own.

**Separate sessions.** This is like having several terminal tabs open, each one a full agent. A session started in a different folder picks up that folder's `CLAUDE.md`, so it gets a different role. I start some myself. Others are started by other agents and run in the background with no window. Sessions talk to each other by message or through shared files.

The rest of the guide uses both kinds. [Many agents on one project](05-multi-agent.md) shows them working together on my main pipeline.
