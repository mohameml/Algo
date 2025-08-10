def dfs_recursif(noeud, visite):
    # if noeud not in visite:
    #     visite.add(noeud)
    #     print(noeud)  # Traitement
    #     for voisin in graphe[noeud]:
    #         dfs_recursif(voisin, visite)
    
    # visite.add(noeud)
    print(noeud)  # Traitement
    for voisin in graphe[noeud]:
        dfs_recursif(voisin, visite)

# Exemple d'usage
graphe = {
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': []
}

dfs_recursif('A', set())