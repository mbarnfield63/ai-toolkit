---
title: tdd
description: Matt Pocock's test-driven development skill, which gives the agent a failing test to pass instead of "looks right".
order: 11
---

# tdd

Skill, from Matt Pocock's skills plugin. Status: `occasional`.
Source: [mattpocock/skills](https://github.com/mattpocock/skills).

## What it is

The red, green, refactor loop. The agent writes a test that pins down what the code should do and watches it fail. Then it writes the least code that makes it pass, and tidies up with the test as a safety net. The skill adds guidance on what makes a test worth keeping: test behaviour through the public interface, not the internals, so the test survives a rewrite.

## Why I use it

A lot of research pipeline code has a contract I know before it is written: given these quantum numbers, return this label. For that kind of code, a test is a better target for the agent than my description. A test passes or it doesn't, which rules out code that looks right but is wrong.

I don't use it for everything. For exploratory work, where I don't yet know what the output should be, I write the code first and test it after.

## How I set it up

It comes in the same plugin as [grilling](grilling.md). I start it with `/tdd` and a description of the behaviour I want.
