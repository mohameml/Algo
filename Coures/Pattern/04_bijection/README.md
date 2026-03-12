## Pattern Algorithmique : Vérifier une Bijection entre deux itérables

### 1. Définition

Une **bijection** est une correspondance **un-à-un (1-1)** entre les éléments de deux ensembles.

Cela signifie :

* chaque élément de **A** correspond à **un seul élément de B**
* chaque élément de **B** correspond à **un seul élément de A**

Autrement dit :

* pas deux éléments de **A** → même élément de **B**
* pas deux éléments de **B** → même élément de **A**

En algorithmique (LeetCode / interviews), ce problème apparaît souvent lorsqu’on doit vérifier si **deux structures suivent le même pattern**.

---

### 2. Syntaxe / Template Python

On utilise **deux dictionnaires** pour garantir la bijection :

* `A -> B`
* `B -> A`

```python
map_a_to_b = {}
map_b_to_a = {}

for a, b in zip(A, B):

    if a in map_a_to_b and map_a_to_b[a] != b:
        return False

    if b in map_b_to_a and map_b_to_a[b] != a:
        return False

    map_a_to_b[a] = b
    map_b_to_a[b] = a

return True
```

**Complexité**

* Temps : `O(n)`
* Mémoire : `O(n)`

---

### 3. Exemple

#### Problème

```
pattern = "abba"
s = "dog cat cat dog"
```

On veut vérifier si le **pattern correspond aux mots**.

---

#### Étapes

| pattern | word | mapping |
| ------- | ---- | ------- |
| a       | dog  | a → dog |
| b       | cat  | b → cat |
| b       | cat  | ok      |
| a       | dog  | ok      |

Résultat :

```
True
```

---

#### Cas invalide

```
pattern = "abba"
s = "dog cat cat fish"
```

| pattern | word | mapping   |
| ------- | ---- | --------- |
| a       | dog  | a → dog   |
| b       | cat  | b → cat   |
| b       | cat  | ok        |
| a       | fish | ❌ conflit |

Résultat :

```
False
```

---

### 4. Problèmes classiques utilisant ce pattern

* Isomorphic Strings : 205
* Word Pattern : 290

Ces deux problèmes sont **structurellement identiques** : vérifier une bijection entre deux séquences.

---

✅ **À retenir**

Si un problème parle de :

* *pattern*
* *mapping*
* *correspondance*
* *isomorphic*

→ penser immédiatement :

```
bijection → deux dictionnaires
```
