# Pattern 01 :Read Pointer / Write Pointer Pattern (Arrays)

## 1. Principe :

> Utiliser **deux pointeurs** pour modifier un tableau **in-place** sans créer de nouvelle structure.

- **read** : parcourt tous les éléments
- **write** : indique où écrire le prochain élément valide

👉 `read` lit tout, `write` écrit uniquement ce qu’on conserve.

- **À tout moment :**
    - `nums[0:write]` → éléments valides
    - `nums[write:read]` → zone écrasable
    - `nums[read:]` → éléments non encore lus

## 2. **Exemple (Remove Element):**

```python
nums = [0,1,2,2,3,0,4,2]
val = 2

write = 0
for read in range(len(nums)):
    if nums[read] != val:
        nums[write] = nums[read]
        write += 1

# Résultat : nums[:write] = [0,1,3,0,4]
# write = 5
```

## 3. Quand utiliser ce pattern

- filtrer des éléments
- supprimer sans `remove()`
- compacter un tableau
- modifier **in-place** en O(1) mémoire

## 4. Problèmes LeetCode similaires

- **27** – Remove Element
- **26** – Remove Duplicates from Sorted Array
- **283** – Move Zeroes
- **88** – Merge Sorted Array
- **977** – Squares of a Sorted Array
- **844** – Backspace String Compare
