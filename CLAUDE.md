# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal algorithms & data structures learning repository. Content is in French and English. Covers theory (courses), LeetCode exercises, and quant interview prep (algo/DS problems with finance context). Primary language is **Python**.

## Repository Structure

- **`Coures/`** — Course notes and implementations:
  - `Algo/` — Algorithm topics (01_introduction through 13_branch_bound)
  - `DS/` — Data structures (01_Array through 11_Tries)
  - `Pattern/` — Coding patterns (two pointers, sliding window, read/write pointers, bijection)
- **`Exercices/`** — Practice problems (leetCode, interviews, openQuant)
- **`Ressources/`** — Supplementary material
- **`Format.md`** — Defines the chapter directory format (read this before creating/restructuring chapters)
- **`template.py`** — Exercise file template

## Chapter Format (see `Format.md` for full details)

Two layouts, both with `README.md` as entry point:

- **Simple chapter**: `README.md` contains course content directly
- **Big chapter**: `README.md` has roadmap + links to `cour/01_module.md`, `cour/02_module.md`, etc.

Both have:
- `exos/Exercices.md` — tracking table (name, difficulty, source, status, key idea)
- `exos/python/01_exo_name.py` — skeleton only (problem statement + function signature + tests)
- `solutions/python/01_exo_name.py` — full implementation (same filename as exo)

## Exercise Sources

- **LeetCode** — referenced as `LC <number>` in Exercices.md
- **Quant Interview** — algo/DS problems with finance context (order books, arbitrage detection, time series, etc.)

## Exercise Template

Files follow `template.py` format: docstring with problem statement + `times`/`last_date` tracking fields, typed function signature, test cases in `__main__`.

## Workflow Rules

- **New or unformatted chapters**: always discuss the content and sections with the user first. Only write/format the chapter after the user validates the proposed structure.
- **DS chapters (`Coures/DS/`)**: always implement data structures from scratch (no library imports like `heapq`, `deque`, etc.) to ensure deep understanding. The first exercise (`01_`) must always be the from-scratch implementation of the DS itself.

## Running Code

```bash
# Run a specific test file
pytest Coures/DS/08_Tree/test_bst.py

# Run a single Python file
python3 Coures/DS/10_Heap/python/cours/MinHeap.py
```
