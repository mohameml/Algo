from __future__ import annotations

# PB 1 : fibo DP1
class Fibo : 
    """
    f_0 = f_1 = 1 

    f_n = f_{n-1} + f_{n-2} for all n >= 2 

    """
    def __init__(self) -> None:
        self.cache = {}

    # méthode naive 
    @classmethod 
    def fibo_naive(cls , n : int) -> int : 
        if n == 0 or n ==  1 : 
            return 1 
        res = cls.fibo_naive(n - 1) + cls.fibo_naive(n - 2)
        return res 


    # méthode Bottom-up 
    @classmethod
    def fibo_bottom_up(cls , n : int) -> int :
        if n == 0 or n == 1 :
            return 1 
        fib = [1]*(n+ 1) 

        for i in range(2 , n + 1) : 
            fib[i] = fib[i-1] + fib[i-2]
        
        return fib[n]


    @classmethod
    def fibo_optim_bottom_up(cls , n : int) -> int:
        if n == 0 or n == 1 :
            return 1 
        prev , curr = 1 , 1 

        for _ in range(2 , n + 1) : 
            temp = curr 
            curr = curr + prev 
            prev = temp 

        return curr 





    # méthode Top-down 
    @classmethod
    def fibo_top_down(cls , n : int) -> int : 

        cache : dict[int , int] = {
            0 : 1 , 
            1 : 1 
        }

        def _fibo(n : int) -> int : 
            if n in cache : 
                return cache[n]
            res = _fibo(n - 1) + _fibo(n - 2)
            cache[n] = res 

            return res 

        return _fibo(n)

