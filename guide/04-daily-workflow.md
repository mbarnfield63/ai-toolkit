---
title: A normal day
description: How work moves on a normal day, from an idea on my phone to a saved state, with the vault as the hub.
order: 4
---

# A normal day

The vault from the [last page](03-vault-memory.md) is the hub. Nothing depends on one chat window remembering anything.

<!-- FIGURE: slide 5, hub diagram: phone, VaultAgent, me, project agents, GPU cluster around the vault -->

## Five steps

1. **An idea arrives.** Away from my desk, I message VaultAgent from my phone. VaultAgent runs all the time on a home server through Claude Code's [Remote Control](../kit/remote-control.md). A project idea goes into that project's state file under "Pending Ideas". An Instagram reel or GitHub link gets transcribed or summarised into a note and filed the same way.
2. **I get up to speed.** At my desk I open the project in [herdr](../kit/herdr.md) and say "get up to speed". The agent reads the state file, and yesterday's idea is waiting there.
3. **We plan, then work.** For anything big, I run a [grilling](../kit/grilling.md) session first. The agent asks me one question at a time, each with a recommended answer, until we agree on a plan. Then it works.
4. **Heavy jobs go to the cluster.** Jobs like OCR on scanned papers go to the department GPU cluster through my [hypatia](../kit/hypatia.md) cluster skills.
5. **I save state.** At a natural stopping point I say "save state". The vault gets the new state and log, and the commit is made.

## Inside step 3

Step 3 is where most of the time goes. In more detail:

1. Launch Claude Code in the project folder and say "get up to speed".
2. Run `/grilling` with "I want to make [idea]".
3. Write a long, detailed description of what I want, or what is broken.
4. Answer lots of questions, one at a time, until we share an understanding.
5. Confirm the finished plan.
6. The agent writes the code under [ponytail](../kit/ponytail.md)'s rules, which are always on.
7. Commit the changes and say "save state". The [graphify](../kit/graphify.md) hook updates the project's knowledge graph after the commit.
8. Run the code or pipeline, then the tests. For work where the correct behaviour can be stated up front, I use [tdd](../kit/tdd.md), so the agent has a test to pass instead of "looks right".
9. Spawn agents as needed for specific code blocks or pipeline stages, and wait for them to finish.
10. Save state again. The log gets a new entry, and the state file is replaced, so the next session starts from current context, not stale context.

## Why grill first

Clear, detailed prompts are worth the effort up front. Every vague ask costs tokens later, while the agent works out what should have been said at the start. So I interrogate large or unclear asks before any code is written, instead of leaving the model to guess in the middle of the work. This repo was planned that way: a grilling session agreed the layout, the build order and the scrub list before any page was written.

## Choosing a model

- **Sonnet** is my daily driver.
- **Opus or Fable** I choose by the type of task, not the size of the project. I keep them for planning very large changes or refactors, not for "this project is important".
