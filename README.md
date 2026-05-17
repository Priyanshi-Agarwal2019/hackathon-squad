# Hackathon Squad Selection Optimization

## Project Description
This repository contains a high-performance Python solution designed to solve the **Maximum Weight Independent Set (MWIS)** optimization problem under a strict 5-minute execution window. 

Given a pool of up to 200,000 student coders with specific individual skill ratings, the algorithm selects a conflict-free "dream team" that maximizes the total skill rating.

## Algorithm Overview
1. **Greedy Initialization:** Nodes are sorted and filtered by an efficiency metric: Skill / (Degree + 1). This prioritizes high-performing coders with minimal systemic conflicts.
2. **Stochastic Hill Climbing:** The algorithm executes an iterative improvement phase. It tests random state transitions, occasionally accepting suboptimal swaps to escape local minima traps, and tracks the globally optimal team set.

## Repository Structure
* `solution.py` - Main optimization algorithm logic
* `input.txt` - Input dataset matching the hackathon format
* `README.md` - Project documentation

## Setup & Execution
Run the optimization script with the input pipeline:
```bash
Get-Content input.txt | python solution.py
```

## Team Members & Contributors
* **Priyanshi Agarwal** (GitHub ID: priyanshi-agarwal-2019) - Repository Host & Code Implementation
* **Versha** - Algorithm Design & Documentation
