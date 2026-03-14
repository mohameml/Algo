# Chapter Format

Each chapter lives under `Coures/Algo/`, `Coures/DS/`, or `Coures/Pattern/`.
Two layouts exist depending on chapter size. Both share the same entry point: `README.md`.

## Simple Chapter (e.g., binary_search)

```
chapter_dir/
    README.md                   # course content directly
    exos/
        Exercices.md            # tracking table (see below)
        python/
            01_exo_name.py      # skeleton only (see template.py)
    solutions/
        python/
            01_exo_name.py      # full implementation (same filename as in exos/)
```

## Big Chapter (e.g., Graph, Heap)

```
chapter_dir/
    README.md                   # roadmap + links to modules in cour/
    cour/
        01_module_name.md
        02_module_name.md
        ...
    exos/
        Exercices.md
        python/
            01_exo_name.py
    solutions/
        python/
            01_exo_name.py
```

## Exercise Template (`template.py`)

Files in `exos/python/` contain only the skeleton (no solution).
Files in `solutions/python/` contain the full implementation.
Both follow this format:

```python
"""
Exo {exo-number} : {exo-name}
---------------------------------
Statement of exo ...

Examples :
---------------
...

----
times : 1
last_date : 2026-03-14
"""

def name_of_func(a: Type1, b: Type2) -> TypeReturn:
    ...


if __name__ == "__main__":

    # Test 1 :
    ...

    # Test 2 :
    ...
```

- `times` — number of times you have practiced this exercise
- `last_date` — date of last practice (useful for spaced repetition)

## Exercices.md Table Format

Located in `exos/Exercices.md` for each chapter.

```markdown
| # | Name | Difficulty | Source | Status | Key Idea |
|---|------|-----------|--------|--------|----------|
| 01 | binary_search | Easy | LC 704 | done | left/right pointers |
| 02 | order_book_matching | Medium | Quant Interview | done | two heaps (bid/ask) |
```

- **Source**: `LC <number>` for LeetCode, `Quant Interview` for algo/DS problems with finance context (order books, arbitrage, time series, etc.)
- **Status**: `done` or empty
- **Key Idea**: short description of the core technique

## Language

Python only for now. Other language dirs (`rust/`, `csharp/`) can be added later.


## Chapter Content Format

Each chapter README (or module `.md` for big chapters) uses numbered sections.
The sections below are **suggested, not mandatory** — adapt to the topic. Some chapters need more sections (e.g., binary search has multiple implementation variants each with their own section).

### Typical sections

```md
# Chapter : {name-chapter}

## 1. Introduction

> Definition ...

- When to use / How to recognize:
    - ...
    - ...

## 2. Implementation

> Description of the approach

- **Template Code:**

    ```python
    def func(...):
        ...
    ```

- **Complexity:**

    | Type | Value |
    |------|-------|
    | Time | O(...) |
    | Space | O(...) |

- **Edge Cases:**
    - ...

## 3. Examples

3 inline worked examples (easy, easy, medium — classic must-know).
Link to `exos/` for more practice.
```

### Rules

- **Definitions** use `>` blockquotes
- **Sub-sections** when a section is big: `## 3.1 ...`, `## 3.2 ...`
- **Extra bullet points** under a title for additional details:
    ```md
    - point title:
        - detail 1
        - detail 2
    ```
- **When to use / How to recognize** — include in Introduction when relevant (helps for interview pattern recognition, e.g., "use binary search when: sorted array, monotonic condition")
- **Multiple implementation variants** — each gets its own numbered section with: definition, template code, edge cases, example (see `04_binary_search` for reference: lower bound, upper bound, floor/ceil, predicate search, etc.)
- **Quant / Finance applications** — if the topic has real quant trading applications, add a dedicated section (e.g., "Real Quant Applications") with: definition, template code, real use cases
- **Examples** are inline (short, self-contained, showing the pattern). The `exos/` dir is for practice (skeleton only)
- **Data Structures (`Coures/DS/`)** — always implement from scratch (no `import heapq`, no `from collections import deque`, etc.). The goal is to deeply understand the internals of each DS, not just use a library
