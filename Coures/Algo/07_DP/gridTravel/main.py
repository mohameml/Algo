"""

- Considérons une grille m xn (m lignes, n colonnes). 
- Un voyageur est situé dans le coin supérieur gauche de la grille à la position (0,0), 
- et l'objectif est d'atteindre le coin inférieur droit à la position (m-1,n-1). 
- Le voyageur ne peut se déplacer qu'en bas ou à droite.

> L'objectif est de compter le nombre total de façons différentes pour le voyageur d'atteindre le coin inférieur droit.
"""
class GridTravel : 

    @classmethod
    def solve_naive(cls , m :int , n : int) -> int : 
        """
        Phi(m , n) = Phi(m - 1 , n) + Phi(m , n - 1)  
        """

        if m == 0 or n == 0 : 
            return 0 
        if m == 1 and n == 1 : 
            return 1 

        return cls.solve_naive(m - 1 , n) + cls.solve_naive(m , n - 1)

    @classmethod
    def solve_top_down(cls , m : int , n :int) -> int : 

        cache = {}

        def dp(i :int , j : int) -> int : 
            
            if i == 0 or j == 0 : 
                return 0 
            
            if i == 1 and j == 1 : 
                return 1 
            
            if (i,j) in cache : 
                return cache[(i,j)]
            
            cache[(i,j)] =dp(i - 1 , j) + dp(i , j - 1) 

            return cache[(i,j)] 
        return dp(m , n)

    @classmethod
    def solve_bottom_up(cls , m : int , n : int) -> int : 

        if m == 0 or n == 0 : 
            return 0 

        dp = [[0]*(n + 1) for _ in range(m+1)]
        dp[1][1] = 1 

        for i in range(1 , m + 1 ) : 
            for j in range(1 , n + 1) : 
                if i == 1 and j == 1 : 
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m][n]
    
    @classmethod
    def solve_bottom_up_optim(cls ,m : int , n : int) -> int : 
        if m == 0 or n == 0 : 
            return 0 
        row = [0]*(n +1)
        row[1] = 1 
        for _ in range(1 , m + 1):
            for j in range(1 , n + 1): 
                row[j] = row[j] + row[j - 1]

        return row[n]