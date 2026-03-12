## Exercices :

## Easy (5)

| #           | Problem                                    | Pattern  | Key Idea            |
| ----------- | ------------------------------------------ | -------- | ------------------- |
| 703 : DONE  | Kth Largest Element in a Stream            | Top-K    | Min-Heap taille K   |
| 1046 : DONE | Last Stone Weight                          | Max-Heap | Simuler avec `-val` |
| 215 : DONE  | Kth Largest Element in an Array            | Top-K    | Min-Heap taille K   |
| 1337 : DONE | The K Weakest Rows in a Matrix             | Top-K    | nsmallest + key     |
| 2231 :DONE  | Largest Number After Digit Swaps by Parity | Max-Heap | Two heaps séparés   |

## Medium (4)

| #          | Problem                      | Pattern        | Key Idea              |
| ---------- | ---------------------------- | -------------- | --------------------- |
| 347 : DONE | Top K Frequent Elements      | Counter + Heap | Counter + nlargest    |
| 973 : DONE | K Closest Points to Origin   | Top-K          | Min-Heap sur distance |
| 621        | Task Scheduler               | Greedy + Heap  | Max-Heap + cooldown   |
| 295        | Find Median from Data Stream | Two Heaps      | Max-Heap + Min-Heap   |

## Hard (1)

| #   | Problem              | Pattern     | Key Idea                      |
| --- | -------------------- | ----------- | ----------------------------- |
| 23  | Merge K Sorted Lists | K-way Merge | Heap de (val, list_idx, node) |
