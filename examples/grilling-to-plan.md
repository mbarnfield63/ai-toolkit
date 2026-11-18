---
title: From a vague idea to a plan
description: Thirty-three minutes of grilling turned "put my talk on my website" into the design for this repo.
order: 2
---

# From a vague idea to a plan

## Goal

After a talk on my agent setup, I realised I should be making my setup public. I wanted the details talk on my website, in some form, and then some. That was the whole idea. This page is the session that turned it into the plan for this repo, on 17 November 2026.

## Setup used

- [grilling](../kit/grilling.md), from Matt Pocock's skills plugin.
- VaultAgent, my general agent, which runs in my Obsidian vault. I ran the session there because the result would be a new vault project.
- One Explore subagent, started by the grilling skill to look up facts.

## What I typed

The opening message was one sentence after the skill name:

```
/grilling I'd like to turn this presentation and everything that goes with
it to be a part of my website again. I'd like to first make a new repo to
maintain/update in C/Code, then the website can take that repo and
structure to use within the website.
```

After that, almost everything I typed was an answer: "yes to those", "Q3a", "the rest yes". The two longer messages were the ones that changed the plan (below).

## What the agent did

The skill works in rounds. Each round asks every question that can be answered now, numbers them, and gives a recommended answer worded so that "yes" accepts it. The first round, trimmed:

```
❓ Q1 - What goes in the repo: "Everything that goes with it" could mean:
- (a) the deck itself (.pptx, plus a PDF export)
- (b) the speaker notes as a readable write-up of the talk
- (c) the example files from slides 3 to 5
- (d) the "full kit" list with links to each skill and plugin
- (e) installable copies of your own general skills
- (f) the PowerPoint briefs (v1, v2, v3)

➡️ (a) to (e). Leave out (f): the briefs are build instructions, not
something an audience needs.

❓ Q4 - Where the master copy lives: Right now the deck is a .pptx in
OneDrive.
- (a) The .pptx stays the master. The repo holds exported copies.
- (b) The .pptx moves into the repo and becomes the master.
- (c) Markdown in the repo becomes the master.

➡️ (b). PowerPoint stays the editor, and git tracks each version.
```

While I read that, a subagent looked through my website repo. It found something I had forgotten: a hidden "AI toolkit" section I had started earlier in the month and switched off. The agent asked a new question about it rather than guessing.

### Where I changed the plan

The first round showed me the agent had a different project in mind from mine. It was planning a home for slide decks. So I wrote a longer message:

```
I want the information in the slides to be transposed into markdown files
to have a living repository with everything i currently work with/use on a
day to day basis. Both my own skills but also any plugins etc I have
downloaded and keep using like rtk, graphify etc. I don't want to put the
powerpoint up, but some of the figures can be saved as PNGs from the slide
deck if needed.
```

The agent restated what that settled, said which earlier questions were now moot (three of five), and asked a new round. The rest went quickly. Five rounds and about 30 questions in all:

1. What the repo is, and the first scope (above).
2. Public or private, the hidden toolkit section, whether to copy my skills or link them, the folder layout, the format of a kit page.
3. How the website pulls the repo in, how links render on both GitHub and the site, figures, what counts as a kit entry.
4. The status scale, which examples to write, the example template, the scrub list, the build order.
5. A "copy me exactly" install guide, which I asked for in round 4.

The second change was in round 4. The agent proposed five worked examples. I kept two (this page and an orchestrator day, later replaced by [the question that found a bug](solver-fix.md)) and asked for the install guide instead.

At the end it wrote out the full design and waited. I typed "yes, start step 1", and it created the repo, the licence files and the vault project. Thirty-three minutes from the first message to the agreed design.

## What I checked

- Every recommendation. I accepted most of them, but not all. In round 5 the agent recommended publishing scrubbed snapshots of my private config, so the install guide could be exact. I chose "public sources only" instead.
- That facts came from lookups, not from me. The skill says finding facts is the agent's job. It checked my GitHub repos, the website's build and its plugins itself.
- The final design, before saying yes. It went into the vault as a plan file, which every later session reads.

## What went wrong, and what I'd change

- My opening message was too thin. One more paragraph about what I wanted (a living record of my setup, no decks) would have saved the first round.
- The plan was right about the shape but not every detail. In review I later cut two guide pages it proposed, and its slide numbers went stale when the deck grew. A plan file you can edit is what makes that cheap: each change is one line, and [save-state](../kit/save-state.md) keeps it in step with the state file.

## Related

- [A normal day](../guide/04-daily-workflow.md): where grilling sits in the loop.
- [grilling](../kit/grilling.md): how to install it and what the rounds look like.
- [Vault memory](../guide/03-vault-memory.md): the plan, state and log files the session created.
