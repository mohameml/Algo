"""

## **Clone Graph (LeetCode 133) - Moyen**

### **Énoncé**

Étant donné une référence d'un nœud dans un **graphe non-dirigé connecté**, retournez une **copie profonde** (clone) du graphe.

Chaque nœud contient :
- `val` : valeur du nœud
- `neighbors` : liste des voisins

**Input :**
```
adjList = [[2,4],[1,3],[2,4],[1,3]]
```

**Visualisation :**
   1 --- 2
   |     |
   4 --- 3

**Output :**  Copie profonde du graphe

"""

from typing import Optional , Dict ,List
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



Graph = Dict[int , List[int]]
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        Clone un graphe en utilisant DFS
        
        Args:
            node: référence du premier nœud
        
        Returns:
            Référence du nœud cloné
        
        Complexité: O(V + E)
        """
        if not node : 
            return None 

        old_to_new = {node : Node(node.val)}
        queue = deque([node])

        while queue : 
            curr_node = queue.popleft()

            for nei in curr_node.neighbors : 
                if nei not in old_to_new : 
                    old_to_new[nei] = Node(nei.val)
                    queue.append(nei)
                old_to_new[curr_node].neighbors.append(old_to_new[nei])

        return old_to_new[node]

# Helper pour tester
def build_graph(adj_list):
    if not adj_list:
        return None
    
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            nodes[i].neighbors.append(nodes[neighbor - 1])
    
    return nodes[0]

# Test
sol = Solution()
graph = build_graph([[2,4],[1,3],[2,4],[1,3]])
cloned = sol.cloneGraph(graph)
print(cloned.val if cloned else None)  # 1


### **Indices** 💡

# <details>
# <summary>Indice 1</summary>

# Utilisez un dictionnaire pour mapper les nœuds originaux vers les nœuds clonés : `{original: clone}`.

# </details>

# <details>
# <summary>Indice 2</summary>

# DFS : 
# 1. Si le nœud est déjà cloné, retourner le clone
# 2. Sinon, créer un nouveau nœud
# 3. Cloner récursivement tous les voisins

# </details>
