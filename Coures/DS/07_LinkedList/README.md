# Chapter : LinkedList

## Overview

> Une **Linked List** (liste chaînée) est une structure de données linéaire où chaque élément (**noeud**) contient une valeur et un pointeur vers le nœud suivant. Contrairement aux arrays, les éléments ne sont **pas contigus en mémoire**.

- When to use / How to recognize:
    - Insertions/suppressions fréquentes en O(1) (si on a le pointeur)
    - Pas besoin d'accès par index
    - Taille inconnue à l'avance
    - Problèmes impliquant des pointeurs, fusion, inversion, détection de cycle

- Comparaison Array vs LinkedList:

    | Opération | Array | LinkedList |
    |-----------|-------|------------|
    | Access by index | O(1) | O(n) |
    | Insert at head | O(n) | O(1) |
    | Insert at tail | O(1) amorti | O(1) avec tail pointer |
    | Insert at middle | O(n) | O(1) si on a le pointeur |
    | Delete | O(n) | O(1) si on a le pointeur |
    | Search | O(n) | O(n) |
    | Memory | Contigu, cache-friendly | Non contigu, overhead par nœud |

## Roadmap

| # | Module | Description |
|---|--------|-------------|
| 01 | [Singly Linked List](cour/01_singly_linked_list.md) | Définition, node, implémentation from scratch (insert, delete, search, traversal), complexité, edge cases |
| 02 | [Doubly Linked List](cour/02_doubly_linked_list.md) | DLL node, implémentation from scratch, traversal bidirectionnel, complexité, edge cases |
| 03 | [Common Techniques](cour/03_common_techniques.md) | Two pointers (slow/fast), dummy head, reverse, merge sorted lists, cycle detection (Floyd), complexité, edge cases |
| 04 | [Advanced Operations](cour/04_advanced_operations.md) | Reorder list, deep copy with random pointer, LRU Cache, complexité, edge cases |

## Exercises

See [exos/Exercices.md](exos/Exercices.md) for the full exercise list.
