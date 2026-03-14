# Plan Interview BNP — Algo & DS & Brainteaser

## 3-Day Review Plan

### Day 1 — DS + Recursion + Sorting

| Priority | Chapter | Focus |
|----------|---------|-------|
| 1 | `DS/01_Array` | basics, dot product |
| 2 | `DS/03_HashMap` | dictionary internals |
| 3 | `DS/07_LinkedList` | implement from scratch, count elements |
| 4 | `DS/04_Stack` | basics |
| 5 | `Algo/03_recurrsion` | fibonacci recursive/iterative/memo |
| 6 | `Algo/05_sorting` | bubble, insertion, merge, quick + **counting sort** + why n log n |

### Day 2 — Binary Search + DP + Backtracking

| Priority | Chapter | Focus |
|----------|---------|-------|
| 1 | `Algo/04_binary_search` | review (already formatted) |
| 2 | `Algo/07_DP` | subset sum, partition equal subset, Kadane's max subarray |
| 3 | `Algo/08_backtracking` | N-Queens problem |

### Day 3 — Graph + Review + Mock

| Priority | Chapter | Focus |
|----------|---------|-------|
| 1 | `DS/09_Graph` | Dijkstra (principle + code) |
| 2 | Review key problems | fibonacci, 3 sorts, Dijkstra, N-Queens, max subarray, buy/sell stock |
| 3 | `Pattern/01_Two_pointers` | quick review |


## Exercises to Solve

### Algo & DS Exercises

| # | Exercise | Source | Topic | Difficulty | Status | Key Idea |
|---|----------|--------|-------|-----------|--------|----------|
| 01 | Fibonacci récursif + itératif + complexité | KOLAB + Email | Recursion/DP | Easy | | memo O(n), iterative O(n), recursive O(2^n) |
| 02 | Produit scalaire entre deux vecteurs + complexité | Email | Array | Easy | | O(n) linear scan |
| 03 | Liste chainée : nb d'éléments + complexité + optimisation | Email | LinkedList | Easy | | O(n), keep size counter → O(1) |
| 04 | Trier une liste d'entiers entre 1 et 100 (10M éléments) | KOLAB + Email | Sorting | Easy | | Counting sort O(n) |
| 05 | 3 algorithmes de tri + expliquer + complexités | KOLAB + Email | Sorting | Medium | | insertion O(n²), merge O(n log n), quick O(n log n) avg |
| 06 | Pourquoi quick sort et merge sort sont O(n log n) ? | KOLAB + Email | Sorting | Medium | | log n levels × n work per level |
| 07 | Algorithme de dichotomie : expliquer + code | KOLAB | Binary Search | Easy | | lower/upper bound pattern |
| 08 | Dijkstra : principe + implémentation | KOLAB | Graph | Medium | | priority queue + relaxation |
| 09 | N-Queens (échiquier 8×8, 10 reines) | KOLAB | Backtracking | Medium | | place row by row, check diagonals |
| 10 | Partition array en 2 sous-tableaux de même somme | KOLAB | DP | Medium | | subset sum = total/2 |
| 11 | Toutes les partitions d'un tableau sommant à x | KOLAB | Backtracking/DP | Medium | | backtracking with sum target |
| 12 | Plus grande somme d'éléments consécutifs (max subarray) | KOLAB | DP/Pattern | Medium | | Kadane's algorithm O(n) |
| 13 | Best time to buy and sell stock | KOLAB | Array/DP | Easy | | track min price, max profit — LC 121 |
| 14 | Carte A67B : vérifier la règle (derrière chaque voyelle il y a un nombre pair) | Email | Logic | Easy | | only check vowels and odd numbers |

### Brainteaser Questions

| # | Question | Source | Status |
|---|----------|--------|--------|
| 01 | Vitesse du 1er tour de stade à 15km/h. Quelle vitesse pour le 2nd tour pour que la moyenne des 2 tours = 30km/h ? | Email | |
| 02 | Règle graduée de 1cm cassée en deux : espérance du milieu de la partie la plus longue ? | KOLAB | |
| 03 | Pile ou face : espérance du nombre de deux piles consécutives (affilés) ? | KOLAB | |
| 04 | 3 points uniformes sur le cercle unité : probabilité que le centre soit dans le triangle ? | KOLAB | |

> **Réponse Brainteaser 01** : Impossible. Distance d = tour de stade. Temps 1er tour = d/15. Pour moyenne 30km/h sur 2d, temps total = 2d/30 = d/15. Donc temps restant pour le 2nd tour = 0. Il faudrait une vitesse infinie.


## Interview Context

- **Poste** : R&D BNP Paribas — Global Markets Quantitative Research (GMQR), Resources and Financing Optimization
- **Entretien avec** : Clément Mosser — focus sur IT/Algo et Brainteaser
- **Stack** : Python et C#
- **Domaine** : collateral optimization, liquidity indicators (LCR, NSFR), regression testing
