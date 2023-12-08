def recherche_dichotomique(ensemble_de_donnees, element_recherche):
    debut = 0
    fin = len(ensemble_de_donnees) - 1
    
    while debut <= fin:
        milieu = (debut + fin) // 2
        
        if ensemble_de_donnees[milieu] == element_recherche:
            return milieu  # L'élément recherché a été trouvé à l'indice milieu.
        elif ensemble_de_donnees[milieu] < element_recherche:
            debut = milieu + 1  # Réduire la plage de recherche à la moitié supérieure.
        else:
            fin = milieu - 1  # Réduire la plage de recherche à la moitié inférieure.
    
    return -1  # L'élément recherché n'est pas présent dans l'ensemble de données.

# Exemple d'utilisation :
ensemble = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 5
resultat = recherche_dichotomique(ensemble, element)
if resultat != -1:
    print(f"L'élément {element} a été trouvé à l'indice {resultat}.")
else:
    print(f"L'élément {element} n'a pas été trouvé dans l'ensemble de données.")
