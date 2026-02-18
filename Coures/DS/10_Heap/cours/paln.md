## Plan d'étude : Heap

### Module 1 — Fondamentaux & Théorie

1. Qu'est-ce qu'un Heap ? (Max-Heap, Min-Heap)
2. Propriétés : structure de tas, heap property
3. Représentation en tableau (formules parent/enfant)
4. Complexités : insert O(log n), extract O(log n), build O(n), peek O(1)

### Module 2 — Implémentations from Scratch

1. **Min-Heap** (implémentation complète)
    - `insert` + `heapify_up`
    - `extract_min` + `heapify_down`
    - `peek`, `size`, `is_empty`
2. **Max-Heap** (adaptation)
3. **Heap générique** avec comparateur custom
4. **Build Heap** from array — Floyd's algorithm O(n)
5. **Heap Sort** from scratch
6. **K-ary Heap** (ternaire, etc.)
7. **Min-Max Heap** (double-ended)
8. **Indexed Priority Queue** (update/decrease-key) → crucial pour Dijkstra

### Module 3 — Patterns d'Interview (les 6 patterns fondamentaux)

| #   | Pattern                   | Description                       |
| --- | ------------------------- | --------------------------------- |
| 1   | **Top K Elements**        | Maintenir un heap de taille K     |
| 2   | **K-way Merge**           | Fusionner K listes triées         |
| 3   | **Two Heaps**             | Max-heap gauche + Min-heap droite |
| 4   | **Sliding Window + Heap** | Median ou max dans une fenêtre    |
| 5   | **Greedy + Heap**         | Scheduling, tasks, meetings       |
| 6   | **Graph + Heap**          | Dijkstra, Prim's MST              |

### Module 4 — Problèmes Classiques par Pattern

**Pattern 1 : Top K Elements**

- Kth Largest Element in Array (LC 215)
- Top K Frequent Elements (LC 347)
- K Closest Points to Origin (LC 973)
- Find K Closest Elements (LC 658)

**Pattern 2 : K-way Merge**

- Merge K Sorted Lists (LC 23)
- Kth Smallest in Sorted Matrix (LC 378)
- Smallest Range Covering K Lists (LC 632)

**Pattern 3 : Two Heaps**

- Find Median from Data Stream (LC 295) ⭐ classique absolu
- Sliding Window Median (LC 480)

**Pattern 4 : Sliding Window + Heap**

- Sliding Window Maximum (LC 239) _(déque mais variante heap existe)_
- Meeting Rooms II (LC 253)

**Pattern 5 : Greedy + Heap**

- Task Scheduler (LC 621)
- Reorganize String (LC 767)
- IPO / maximize capital (LC 502)
- Minimum Cost to Connect Sticks (LC 1167)
- Car Pooling (LC 1094)

**Pattern 6 : Graph + Heap**

- Network Delay Time / Dijkstra (LC 743)
- Path with Minimum Effort (LC 1631)
- Swim in Rising Water (LC 778)
- Prim's MST (LC 1584)

### Module 5 — Variantes Avancées

1. **Lazy Deletion** (marquer éléments supprimés sans restructurer)
2. **Fibonacci Heap** (théorie — Dijkstra optimal O(E + V log V))
3. **Binomial Heap** (théorie)
4. **Median Maintenance** structure complète
5. **Priority Queue avec mise à jour de clé**

### Module 6 — Questions Quant/BNP Style

- Ordre de complexité des opérations (pourquoi build est O(n) et pas O(n log n) ?)
- Différence Heap vs BST vs Sorted Array
- Quand utiliser un Heap vs un Segment Tree ?
- Implémenter un scheduler de tâches avec priorités
