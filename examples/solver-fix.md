---
title: The question that found a bug
description: A routine rerun of my CO2 quantum-number pipeline, two follow-up questions, and a one-line solver change that closed a 27-point coverage gap.
order: 1
---

# The question that found a bug

## Goal

One of my papers uses a graph neural network (GNN) to assign quantum numbers to computed energy levels of CO2, across 12 isotopologues. In August 2026 I was answering reviewer's questions and enacting necessary edits. One planned change added a new input feature, `tot_sym`, the symmetry species of each level, and the whole pipeline had to be rerun to refresh the paper's numbers.

The goal for the day was simple: rerun the pipeline, put the new numbers into the paper. This page is that session, on 19 August 2026, trimmed from the logs. It is a single agent, not the [orchestrator](../guide/05-multi-agent.md), and the part worth reading is where my questions changed what it did.

## Setup used

- Claude Code in the project repo, with the "get up to speed" rule in its `CLAUDE.md` (this was before it became the [get-up-to-speed](../kit/get-up-to-speed.md) skill) and a state file in my vault.
- A local GPU for training. The full pipeline trains the model five times, once per bootstrap generation, which takes about 30 minutes.
- Background tasks, so the agent could start a run, check on it, and tell me when it finished.
- The reviewer-response plans from earlier sessions, one Markdown file per planned change.

## What I typed

A handful of short messages over about five hours. These are the ones that mattered:

```
Cuda should be enabled right now, check then run pipeline
```

```
what was the outcome on assigning 727/737 levels? Improved since previous
runs due to the inclusion of tot_sym?
```

```
was the point of this plan and rerun not to include tot_sym across the
pipeline and then see if it improved coverage in the 7s?
```

```
was the tot_sym not added to the solver grouping key? would that not
improve coverage?
```

```
go ahead, scope and build it
```

```
yes do that, revert, kill, and rerun
```

## What the agent did

### 1. The rerun, and the mess around it

Getting one clean run took two and a half hours. The pipeline itself worked. Everything around it did not:

- The first run failed in seconds. The pipeline script does not rebuild the dataset, so the agent ran the dataset step first, as the project's `CLAUDE.md` lists. The next failure was a Windows console encoding error, fixed with an environment variable.
- The final save failed twice with `PermissionError: [Errno 13]` on the 532 MB output file. The agent changed the save to write a temporary file and rename it, which also failed. It then found an orphaned `cmd` process from an earlier crash holding the file open. Auto mode blocked it from killing that process, so it asked me first.
Then it ran the metrics and saved the state file. Routine so far.

Later, a second script needed for other numbers in the paper turned out to be out of date with the model code. The agent fixed three stale calls, one per failed run, then hit process kills it could not explain, and parked it.

### 2. My question, and its answer

Two of the 12 isotopologues, 727 and 737 (CO2 with two oxygen-17 atoms), had always had far fewer levels assigned than the others. The paper explained this away as a limitation. So I asked whether the new feature had helped. The agent's answer:

```
Direct answer: no, tot_sym didn't fix the 727/737 shortfall.

| iso | coverage % |
|-----|------------|
| 626 | 73.5       |
| 636 | 69.2       |
| 727 | 43.7       |
| 737 | 42.7       |
| 828 | 67.1       |
| 838 | 62.6       |

tot_sym only entered the model as an input feature, it was never wired
into the Hungarian solver's grouping key, so it can't split the
doubled-class-count blocks that cause the shortfall. Expected result,
confirmed.
```

I pushed back: wasn't that the point of the rerun? It held its ground:

```
Fair pushback, let me correct the framing.

No. The point of adding tot_sym was never to fix 727/737 coverage. That's
a documented, separate limitation. Fixing coverage would mean adding
tot_sym to the grouping key itself — a bigger, different change,
discussed last session but explicitly not made.
```

The agent was right about what the plan said. But the plan had stopped short, and I wanted to know why.

### 3. The second question

After the model predicts, a solver assigns each level a unique label. It works in blocks: all levels that share an isotopologue, a rotational quantum number J, a parity and a polyad compete for the same set of labels. For 727 and 737, each block holds levels of two symmetry species, roughly twice as many as for the others, all competing for the same slots.

So I asked whether adding `tot_sym` to the block key would help. This time the agent checked the data before answering:

```
Real answer, not guesswork this time: checked MARVEL ground truth directly
for 727/737 blocks with multiple tot_sym species present (743 such
blocks). In every single one, the two species get distinct class IDs —
never the same label.

So: yes, adding tot_sym to the grouping key would plausibly help, but
doing it correctly needs two changes together:
1. groupby(["isotope_id", "J", "parity_encoded", "polyad_int"])
   -> add "tot_sym"
2. build the pool of valid labels per (polyad, tot_sym) instead of per
   polyad alone

This touches the core solver logic behind every number in the paper,
though, so want me to scope and build it, or hold off?
```

### 4. Build, over-correct, revert

I said go. It made both changes and started the full rerun. Instead of waiting 30 minutes for the end, it checked the first generation's numbers after about five:

```
Assignment rate dropped hard (23.5% vs ~47% before) and mean valid classes
per block fell 17.2 -> 6.2 — the fix over-corrected. Assignment rate
collapsed everywhere (626 73.5% -> 40.7%), and 727/737's relative gap to
the others didn't close.

Scoping the class pool by species was too strict. The grouping-key split
(#1) should still help on its own. Reverting just the pool-scoping part.
```

I said "revert, kill, and rerun". With only the block key changed, the first generation already showed the gap closing, and the full run held it:

```
| iso | coverage % |
|-----|------------|
| 626 | 73.53      |
| 636 | 69.16      |
| 727 | 70.65      |
| 737 | 68.79      |
| 828 | 67.10      |
| 838 | 62.55      |

727/737 (previously the two worst, ~43%) now sit mid-pack with everyone
else, no collateral damage elsewhere. Pooled metrics also improved:
94.55% perfect 4-QN match (was 93.80%), mean MAE 0.0652 (was 0.0762).
```

The four other isotopologues barely moved (626 by 0.01 points, the rest not at all), which is what you would expect: their blocks only ever held one species, so the new key changed nothing for them.

The change itself is one line in the solver:

```python
grouped = df.groupby(
    ["isotope_id", "J", "parity_encoded", "polyad_int", "tot_sym_cat"]
)
```

It went in the next day as its own commit, and the paper's section on 727 and 737 now explains the fix instead of the limitation.

## What I checked

- The table after every run. The fix was only believable because four isotopologues stayed exactly the same while two moved.
- The agent's claim that the two species never share a label. It checked that against the measured (MARVEL) levels, not the model's output, which is the right source.
- That it reverted only the half that hurt. The comment it left in `build_polyad_class_map` records the failed attempt and its numbers, so nobody tries it again.

## What went wrong, and what I'd change

- The agent defended the plan instead of the goal. Its first two answers were accurate about what the plan said, and it would have moved on. The fix came from me asking a domain question it could then check. Plans written by earlier sessions carry their assumptions forward, and this agent did not question its plan until I did.
- The first fix had a second part nobody needed. It was a reasonable guess, and the early check caught it in five minutes. That habit, looking at the first generation before waiting for all five, saved about half an hour per wrong turn.
- Most of the day went on the environment. A file lock, an orphaned process and a stale script cost more time than the science. The agent handled all of it, and the one irreversible step, killing a process, waited for me.
- The paper's original explanation was wrong. "A limitation of the method" was really a bug. A limitation written up with an agent's help is worth testing once more before submission.

## Related

- [A normal day](../guide/04-daily-workflow.md): the session loop this fits into.
- [Vault memory](../guide/03-vault-memory.md): the state file that carried the plans between sessions.
