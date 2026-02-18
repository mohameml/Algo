#!/usr/bin/env python3




def distance_levenshtein(seq1 , seq2):

    n = len(seq1)
    m = len(seq2)

    mat_leven = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # 1 ere ligne 

    for i in range(n+1):
        mat_leven[i][0] = i
    
    # 1ere colonne :

    for j in range(m+1):
        mat_leven[0][j] = j

    
    # Algo :

    for i in range(1 , n+1) :
        for j in range(1, m+1) :
            if seq1[i - 1] == seq2[j -1 ] :
                mat_leven[i][j] =  mat_leven[i-1][j-1] 
            else :
                mat_leven[i][j] = 1 + min(mat_leven[i-1][j-1] , mat_leven[i][j-1] , mat_leven[i-1][j]  )


    
    return mat_leven[n][m]


# Test :

print("------------- Test de l'algo de calcul de la distance de levenshtien -----------------------")

seq1 = "chien"
seq2 = "chienne"
distance = distance_levenshtein(seq1, seq2)
print(f"Distance de Levenshtein entre '{seq1}' et '{seq2}' : {distance}")


seq1 = "chien"
seq2 = "chienne"
distance = distance_levenshtein(seq1, seq2)
print(f"Distance de Levenshtein entre '{seq1}' et '{seq2}' : {distance}")


seq1 = "exemple"
seq2 = "sample"
distance = distance_levenshtein(seq1, seq2)
print(f"Distance de Levenshtein entre '{seq1}' et '{seq2}' : {distance}")
# Sortie attendue : Distance de Levenshtein entre 'exemple' et 'sample' : 3


seq1 = "algoritme"
seq2 = "agolrtime"
distance = distance_levenshtein(seq1, seq2)
print(f"Distance de Levenshtein entre '{seq1}' et '{seq2}' : {distance}")
# Sortie attendue : Distance de Levenshtein entre 'exemple' et 'sample' : 3
