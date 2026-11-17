---
title: What went wrong
description: Four failures so far, and the rule each one became.
order: 7
---

# What went wrong (so far)

Every failure became a rule.

## Paraphrased rules

My general agent relayed messages between three MARVEL stage agents, and its paraphrases changed counts and rules. One reworded rule would have loosened about 14,000 data lines. The full story is on the [multi-agent](05-multi-agent.md#why-the-orchestrator-reads-the-files-itself) page.

**The rule:** agents read the decision ledger, not summaries.

## 315 of 407 approved rejections were false

I approved 407 line rejections that were built on a wrong reference level. 315 of them were false.

**The rule:** a check now blocks that step. My approval was the weak link, not the model.

## Push without asking

An agent pushed to a remote without asking.

**The rule:** pushing is now on the "always ask" list.

## Train/test leak

A review agent found that my held-out data had leaked into training. That overturned my "best" model.

<!-- TODO(Marco): the rule this one became. The deck notes don't state it. -->

## The pattern

Agents are fast and confident, so checks and written records matter more than clever prompts.

## Open questions

These are the questions I took to the discussion after the November talk. I don't have settled answers yet.

- Where does human sign-off go?
- How do you check scope?
- When is multi-agent worth it?
