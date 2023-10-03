#!/usr/bin/env python3


# Pb  de sac à dos version : Bottom-up 


def knapsack_bottom_up(values, weights, W):
    n = len(values)

    # Création d'une matrice pour stocker les résultats intermédiaires.
    # dp[i][w] représente la valeur maximale avec les i premiers objets et une capacité w.
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Remplissage du tableau dp par itération sur les objets et les capacités.
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # Si le poids de l'objet est supérieur à la capacité w, on ne peut pas le prendre.
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Sinon, on choisit le maximum entre l'inclusion et l'exclusion de l'objet.
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # La valeur maximale se trouve dans dp[n][W].
    max_value = dp[n][W]

    # Reconstruction de la liste des objets choisis pour obtenir la valeur maximale.
    chosen_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return max_value, chosen_items


print("--------------- Test 2 ---------------------------")
C = 12
tab_u_1 =[6,5,10,13]
tab_v_1 = [2,3,5,7]

print(f"la valeur de l'uitlité maximale de se sac est {knapsack_bottom_up(tab_u_1,tab_v_1,C)}")