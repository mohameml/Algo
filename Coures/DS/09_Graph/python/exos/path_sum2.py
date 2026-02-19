"""
## **Exercice 3 : Path Sum II (LeetCode 113) - Moyen**

### **Énoncé**

Étant donné la racine d'un arbre binaire et un entier `targetSum`, retournez **tous les chemins racine-feuille** où la somme des valeurs du chemin égale `targetSum`.

**Input :**

        5
       / \
      4   8
     /   / \
    11  13  4
   /  \    / \
  7    2  5   1

targetSum = 22

**Output:**

[[5,4,11,2], [5,8,4,5]]


"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Trouve tous les chemins racine-feuille avec la somme cible
        
        Args:
            root: racine de l'arbre
            targetSum: somme cible
        
        Returns:
            Liste de tous les chemins valides
        
        Complexité: O(N) où N = nombre de nœuds
        """
        
        if not root : 
            return []
        
        stack = [(root , 0 , [])]
        res = []
        while stack : 
            node , curr_sum , path = stack.pop()
            curr_sum += node.val 
            path.append(node.val)

            if curr_sum == targetSum : 
                res.append(path.copy())
            
            if node.right : 
                stack.append((node.right , curr_sum , path[:]))
            if node.left : 
                stack.append((node.left , curr_sum , path[:]))
        
        return res



# Test
sol = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print(sol.pathSum(root, 22))
# [[5, 4, 11, 2], [5, 8, 4, 5]]

# Indices 💡
# <details>
# <summary>Indice 1</summary>
# Utilisez DFS avec backtracking. Maintenez un chemin courant et la somme courante.
# </details>
# <details>
# <summary>Indice 2</summary>
# Une feuille est un nœud sans enfants. Vérifiez si node.left is None and node.right is None.
# </details>
