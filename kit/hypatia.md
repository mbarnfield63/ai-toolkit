---
title: hypatia
description: My private skills for sending GPU jobs to my department's cluster and checking on them, with the agent working from my laptop.
order: 10
---

# hypatia

Skills, written by me. Status: `weekly`.
Source: private, because it is specific to one cluster and my account on it.

## What it is

Three skills for Hypatia, the GPU cluster in my department:

- `hypatia` sends a job to the cluster and brings results back.
- `hypatia-squeue` lists my own jobs.
- `hypatia-squeue-all` lists every job on the cluster, so I can see which GPUs are busy before I submit.

The agent always runs on my laptop and drives the cluster over SSH. The cluster is only a job runner. A small submit script copies the working tree of the current repo to the cluster, snapshots it into a timestamped run folder, and queues it with SLURM. Each run folder records the commit, the uncommitted diff and the exact command, so every result can be traced to the code that made it.

## Why I use it

I use the cluster for the heavy jobs: OCR on scanned papers, and training and testing new builds of ML models. Before the skills, every job meant the same manual steps, and every agent had to rediscover the cluster's quirks.

Most of the skill is a list of those quirks, each written down after it went wrong once. Some examples:

- Never edit files on the cluster. The next submit overwrites them.
- Run Python inside the shared container, never on the host. The host's system libraries are too old for current wheels.
- SLURM here doesn't keep GPUs apart, so every job lands on the first GPU unless the job script picks the emptiest one itself.
- Off campus, a timeout on SSH means the VPN is down. Ask me to connect instead of retrying in a loop.

## How I set it up

The skills live in my scripts repo, and `~/.claude/skills/` links to them, so every project can use them. A new project needs a copy of the job template next to its `pyproject.toml` and its inputs pushed once with the data script.

If you have a cluster of your own, I'd write the same kind of skill: the commands to submit and check a job, then every rule you've had to explain to an agent twice.
