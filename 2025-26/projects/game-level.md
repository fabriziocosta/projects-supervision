# Learning to Generate Game Levels via Bayesian Optimisation of Simulated Player Engagement


## Project Summary

**Procedural Content Generation (PCG)** is a central technique in modern game design, enabling the automatic creation of maps, levels, items, and characters. Traditionally, such generation relies on manually tuned heuristics to ensure playability and engagement. However, these handcrafted rules often limit flexibility and adaptability, especially when tailoring content to different player styles.

This project aims to explore a **learning-based approach** to PCG where game level layouts are generated and optimised through a **Bayesian optimisation loop**. The novelty lies in using **simulated agents**, rather than human feedback, to drive the optimisation process. Each game level is abstractly encoded as a **graph or structured representation** (no graphical rendering), and a **lightweight implicit game engine** simulates interactions with various types of AI players.

The overarching goal is to develop a system that **adapts level design to maximise simulated user engagement**, and to study whether this system can learn to differentiate layouts based on **distinct player archetypes** (e.g., explorer, aggressor, speedrunner).

---

## Project Objectives

* Design an abstract encoding scheme for game levels using **graph-based or symbolic representations** (e.g., rooms, paths, obstacles, rewards).
* Implement an **implicit game engine** that simulates how AI-controlled agents (bots) navigate or interact with a level, without visual rendering.
* Define **quantitative metrics of engagement** based purely on interaction traces (e.g., time spent, risk taken, item collection, path diversity).
* Develop a **Bayesian optimisation framework** to iteratively refine level design to maximise engagement metrics for a given player profile.
* Investigate the system’s ability to produce **distinct level types** tailored to different simulated player behaviours.

---

## Technical Scope

The project will involve:

* **Abstract game level design** (e.g., 2D grid world or dungeon-like layouts encoded as graphs or arrays).
* Implementation of **AI players with parameterised behaviours** (e.g., risk-seeking, reward-driven, speed-focused).
* Development of a **simulated game engine** that can:

  * Evaluate agent performance
  * Generate trace logs of decisions, paths taken, and outcomes
* Design of a **player engagement score** derived from trace data (not from questionnaires or surveys).
* Application of **Bayesian Optimisation** (e.g., using Gaussian Processes or Tree-structured Parzen Estimators) to adapt level structure based on feedback from simulated play.
* **Evaluation of the generator’s ability** to produce diverse layouts optimised for contrasting player types.

---

## Learning Outcomes

The student will:

* Gain experience in **procedural content generation** and **optimisation algorithms**.
* Apply **Bayesian inference** and **surrogate modelling** techniques in a real application.
* Design and analyse **simulated environments and AI agents** to mimic user behaviour.
* Develop a robust understanding of **adaptive content generation** and how to design systems that respond to player preferences without human-in-the-loop data.

---

## Expected Deliverables

### A modular codebase implementing:

* Abstract level generator
* Simulated game engine
* Player behaviour models
* Engagement metric computation
* Bayesian optimisation loop

### A report including:

* Design methodology
* Experiments comparing layout adaptation for different player types
* Analysis of optimisation performance and layout diversity

---

## Project Scope Limitations

* No **graphical rendering** or visual assets will be developed.
* No **human users** will be involved; all feedback loops will be based on artificial agents.
* The game engine will be **simplified and abstract**, focusing on decision dynamics, not graphics or physics.

---

## Research Questions

* Can we generate **distinct level designs** optimised for different simulated player behaviours?
* Does **Bayesian optimisation** converge on qualitatively different content for different agents?
* Can **trace-based engagement metrics** act as reliable signals for driving procedural generation?

---

## Apply or Ask Questions
[📨 Click here to open an issue](https://github.com/fabriziocosta/projects-supervision/2025-26/issues/new?template=application.yml&title=Application:%20[Your%20Name]%20for%20game-level)

## Current Status
🟢 Accepting interest — 0/5 students
