from __future__ import annotations
from dataclasses import dataclass
from typing import Optional , Iterable , Generator , List ,Any 


@dataclass
class BSTNode : 
    """
    Node d'un Binary Search Tree (BST).

    Attributs
    ---------
    key : Any
        La clé stockée (doit être comparable avec < et >).
    left : Optional[BSTNode]
        Sous-arbre gauche (clés strictement < key).
    right : Optional[BSTNode]
        Sous-arbre droit (clés strictement > key).
    """
    key : Any 
    left : Optional[BSTNode] = None 
    right : Optional[BSTNode] = None 

class BST : 
    """
    Binary Search Tree (BST) "simple" (non auto-équilibré).

    Rappel : un BST impose la propriété d'ordre :
      - toutes les clés du sous-arbre gauche < key
      - toutes les clés du sous-arbre droit > key

    Complexités :
      - Si l'arbre est équilibré (hauteur h ~ log2(n)) :
            search/insert/delete : O(log n)
      - Pire cas (arbre dégénéré, h ~ n) :
            search/insert/delete : O(n)

    Paramètres
    ----------
    iterable : Optional[Iterable[Any]]
        Si fourni, insère toutes les clés dans l'ordre donné.
    allow_duplicates : bool
        Si True, autorise des doublons (par défaut False).
        Ici, si doublons autorisés, on les insère à droite (>=).
    """

    def __init__(
        self,
        iterable : Optional[Iterable[Any]] = None, 
        *,
        allow_duplicates  : bool = False 
    ) -> None:
        
        self.root : Optional[BSTNode] = None 
        self.size : int = 0 
        self.allow_duplicates  : bool = allow_duplicates

        if iterable is not None : 
            for x  in iterable : 
                self.insert(x)


    # ---------- Recherche ----------


    def contains(self, key: Any) -> bool:
        """
        Vérifie si `key` existe dans l'arbre.

        Pourquoi O(log n) ?
        -------------------
        À chaque étape, on compare key au nœud courant et on descend soit
        à gauche soit à droite : on élimine "en gros" la moitié des clés
        si l'arbre est équilibré. Donc on fait ~h comparaisons, où h=hauteur.
        Si h ~ log2(n), alors O(log n). (Sinon O(n) au pire.)
        """
        return self._search_node(key=key) is not None 
    
    def _search_node(self, key: Any) -> Optional[BSTNode]:
        node = self.root 

        while node : 
            if node.key == key : 
                return node 
            
            if key < node.key :
                node = node.left 
            else :             
                node = node.right 
        
        return None 


    # ---------- Insertion ----------

    def insert(self, key: Any) -> None:
        """
        Insère `key` dans le BST.

        Doublons
        --------
        - si allow_duplicates=False : lève ValueError si key existe déjà
        - si allow_duplicates=True  : insère les doublons à droite (>=)

        Complexité
        ----------
        O(h) comparaisons, où h est la hauteur.
        Donc O(log n) si l'arbre est équilibré, O(n) au pire.
        """

        if not self.root :
            self.root = BSTNode(
                key=key,
            )

            self.size = 1 
            return 

        parent : Optional[BSTNode] = None 
        node : Optional[BSTNode] = self.root 

        while node : 
            parent = node 
            if key == node.key and not self.allow_duplicates: 
                raise ValueError(f"key : '{key} already exits'")

            if key < node.key  : 
                node = node.left 
            else : 
                node = node.right

        if not parent : 
            return 

        if key < parent.key : 
            parent.left = BSTNode(key=key)
        else : 
            parent.right = BSTNode(key=key)

        self.size += 1 

    # ---------- Min / Max ----------

    def min(self) -> Any:
        """
        Retourne la plus petite clé.

        Pourquoi O(log n) ?
        -------------------
        On descend toujours à gauche. Nombre d'étapes = hauteur h.
        Donc O(h) -> O(log n) si équilibré.
        """
        min_node = self._min_node(self.root)
        if min_node is None : 
            raise ValueError("BST is empty")
        return min_node.key      


    def max(self) -> Any : 
        """
        Retourne la plus grande clé.

        Même logique que min() : on descend toujours à droite.
        O(h) -> O(log n) si équilibré.
        """
        max_node = self._max_node(self.root)
        if max_node is None : 
            raise ValueError("BST is empty")
        return max_node.key

    def _min_node(self , node :Optional[BSTNode]) -> Optional[BSTNode] : 
        """
        return the ndoe with the min key
        """

        if node is None : 
            return None 

        while node.left : 
            node = node.left
        
        return node 
    def _max_node(self , node : Optional[BSTNode]) -> Optional[BSTNode]:
        if node is None : 
            return None 
        
        while node.right : 
            node = node.right 
        return node 

    # ---------- Suppression ----------

    def delete(self, key: Any) -> bool:
        """
        Supprime `key` si présent. Retourne True si suppression faite, sinon False.

        Cas classiques
        --------------
        1) nœud feuille -> on le retire
        2) nœud avec 1 enfant -> on le remplace par son enfant
        3) nœud avec 2 enfants -> on le remplace par son successeur inorder
            (min du sous-arbre droit), puis on supprime ce successeur)

        Complexité
        ----------
        - Trouver le nœud : O(h)
        - Trouver successeur (cas 3) : O(h)
        Total O(h) -> O(log n) si équilibré, O(n) au pire.
        """
        self.root , deleted = self._delete_rec(self.root , key)
        if deleted : 
            self.size -= 1 
        return deleted

    def _delete_rec(self, node: Optional[BSTNode], key: Any) -> tuple[Optional[BSTNode], bool]:
        # Cas de base : on a atteint un sous-arbre vide
        # -> la clé n'existe pas dans l'arbre
        if node is None:
            return None, False

        # Si la clé à supprimer est plus petite que la clé courante,
        # alors elle se trouve dans le sous-arbre gauche
        if key < node.key:
            node.left, deleted = self._delete_rec(node.left, key)
            return node, deleted

        # Si la clé à supprimer est plus grande que la clé courante,
        # alors elle se trouve dans le sous-arbre droit
        if key > node.key:
            node.right, deleted = self._delete_rec(node.right, key)
            return node, deleted

        # À partir d'ici : key == node.key
        # -> on a trouvé le nœud à supprimer

        # CAS 1 : le nœud est une feuille (aucun enfant)
        # On le supprime simplement
        if node.left is None and node.right is None:
            return None, True

        # CAS 2 : le nœud a uniquement un enfant droit
        # On remplace le nœud par son enfant droit
        if node.left is None:
            return node.right, True

        # CAS 3 : le nœud a uniquement un enfant gauche
        # On remplace le nœud par son enfant gauche
        if node.right is None:
            return node.left, True

        # CAS 4 : le nœud a DEUX enfants
        #
        # Idée clé :
        # - On ne peut pas supprimer directement ce nœud sans casser le BST
        # - On le remplace par son SUCCESSEUR INORDER
        #
        # Le successeur inorder est :
        #   -> la plus petite clé STRICTEMENT plus grande que node.key
        #   -> donc le minimum du sous-arbre droit

        # On commence dans le sous-arbre droit
        curr = node.right

        # On descend le plus à gauche possible
        # pour trouver la plus petite clé du sous-arbre droit
        while curr.left:
            curr = curr.left

        # À ce stade :
        # curr.key est le successeur inorder de node.key

        # On remplace la clé du nœud courant par celle du successeur
        node.key = curr.key

        # Maintenant, il faut supprimer le successeur dans le sous-arbre droit
        # IMPORTANT :
        # - le successeur n'a PAS de fils gauche
        # - donc sa suppression est simple (cas feuille ou 1 enfant)
        node.right, _ = self._delete_rec(node.right, curr.key)

        # On retourne le nœud modifié et True (suppression effectuée)
        return node, True


    # ---------- Successeur / Prédécesseur ----------

    def successor(self, key: Any) -> Optional[Any]:
        """
        Retourne le successeur inorder de `key` (la plus petite clé > key),
        ou None si pas de successeur ou si key n'existe pas.

        Complexité : O(h) -> O(log n) si équilibré.
        """
        succ : Optional[BSTNode] = None 
        node : Optional[BSTNode] = self.root 

        # 1) trouver le node + stocker les ancêtres potentiels
        while node : 
            if key < node.key : 
                succ = node 
                node = node.left 
            elif key > node.key : 
                node = node.right 
            else : 
                break 
        
        if not node : 
            return None 

        # 2) CAS IMPORTANT : sous-arbre droit
        if node.right : 
            curr = node.right 
            while curr.left : 
                curr = curr.left 
            return curr.key 


        return succ.key if succ else None 

    # ---------- Traversées ----------

    def inorder(self) -> List[Any]:
        """
        Retourne la liste des clés en ordre croissant (inorder traversal).

        Complexité : O(n) car on visite chaque nœud exactement une fois.
        """
        return list(self._inorder_gen(self.root))

    def _inorder_gen(self, node: Optional[BSTNode]) -> Generator[Any, None, None]:
        if not node:
            return
        yield from self._inorder_gen(node.left)
        yield node.key
        yield from self._inorder_gen(node.right)

    # ---------- Utilitaires ----------

    def __len__(self) -> int:
        """Retourne le nombre d'éléments dans le BST. O(1)."""
        return self.size

    def __iter__(self) -> Generator[Any, None, None]:
        """Itère sur les clés en ordre croissant. O(n) total."""
        yield from self._inorder_gen(self.root)

    def __repr__(self) -> str:
        return f"BST(size={self.size}, inorder={self.inorder()})"