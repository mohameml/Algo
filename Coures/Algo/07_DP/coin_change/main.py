"""
On te donne :

- une liste de pièces coins = [c1, c2, ..., cn]
- un montant amount

>Trouver le nombre minimum de pièces pour rendre exactement amount.
> Si impossible, retourner -1.

- ex : 
    - coins = [1 , 3 , 4] , amount = 6 
    - res : 2 car 3 + 3 = 6 
"""

from typing import List


class CoinChange : 
    """ 
    - we have : amount and coins = [c_1 , .... , c_N] (N coins)
    - for each c_i we return n_i  so the pb : 
    -  min sum_{i=1}^{N} n_i 
        s.t sum_{i=1}^{M} c_i*n_i == amount 
        s.t n_i == 0 if we don't use c_i 

    - Bellman equation 2D : 
        - we not that Phi(n , A) : the nb min of coins to find  A
        - case 1 take n s.t c_n <= A : Phi(n , A) = min(1 + Phi(n , A - c_n) , Phi(n - 1 , A))
        - case 2 skip n : Phi(n , A) = Phi(n - 1 , A)
        - base case : Phi(n , 0) = 0 , Phi(0 , a) = + ifini 
    
    - Bellman 1D : 
        - 
    """

    @classmethod
    def solve_naive(cls , coins : List[int] , amount : int) -> int : 

        if amount == 0 : 
            return 0 
        
        if not coins : 
            return - 1 

        INF = 2**(32) - 1

        def dp(i :int , a: int) -> int : 
            if a == 0  : 
                return 0 
    
            if i < 0 :
                return INF  

            res = dp(i - 1 , a)
            if coins[i] <= a : 
                res =  min(res , 1 + dp(i , a - coins[i]))
            return res 
        ans = dp(len(coins) - 1 , amount)
        return -1 if ans >= INF else ans 
            

    @classmethod
    def solve_top_down(cls) : 
        """
        
        """

    @classmethod
    def solve_bottom_up(cls) : 
        """ 
        Phi()
        """
        ... 

    @classmethod
    def solve_bottom_up_optim(cls) : 
        """ 
        Phi()
        """
        ... 


if __name__ == "__main__" : 
    coins = [1 , 3 ,  4]
    amount = 6 
    nb_min = CoinChange.solve_naive(coins , amount)
    print(f"nb_min to return {amount} from coins {coins} is : {nb_min}")