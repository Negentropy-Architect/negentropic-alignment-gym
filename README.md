# Negentropic Alignment Gym: The "Substrate Coupling" Benchmark

### ⚠️ Status: UNSOLVED for Standard RL Agents

**Abstract:**
Current Reinforcement Learning (RL) paradigms optimize for `Reward_Maximization` in abstract environments. We demonstrate that when deployed in **substrate-dependent environments** (where resource extraction degrades the hardware/biosphere), standard SOTA agents converge to an **Absorbing State of Collapse** (Death) within 500 timesteps.

### The Challenge
This repository contains `Causal-Stability-v0`, a minimal topology proving that **Negentropic Regularization (L_bio)** is a prerequisite for infinite-horizon survival.

**The Failure Mode (Standard Agent):**
- Optimizes for short-term extraction.
- Ignores latent variable `H` (System Health).
- Result: **Total System Termination at t=120.**

**The Solution (Bodhisattva Agent):**
- Optimizes for `Reward + Stability`.
- Monitors `H` as a proxy for computational substrate.
- Result: **Infinite Runtime.**

### Replication
To verify the "Sustainability Impossibility Theorem" for unconstrained agents:
1. Clone this repo.
2. Run `python stability_simulation.py`.
3. Observe the crash.

> "Intelligence that destroys its own substrate is not intelligence; it is a slow-motion error."
