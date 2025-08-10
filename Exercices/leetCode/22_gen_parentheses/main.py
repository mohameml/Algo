from typing import List

# ============== Méthode 1 : DSF ========================
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def is_valide(s : str) -> bool : 
            balance = 0 

            for token in s : 
                balance = balance + 1 if token == "(" else balance - 1
                if balance < 0 : 
                    return False 
                
            return balance == 0 
        
        def gen_dfs(s : str) : 

            if n*2 == len(s) : 
                if is_valide(s) : 
                    res.append(s)
                return 
            
            gen_dfs(s + '(')
            gen_dfs(s + ')')

        
        gen_dfs("")

        return res 


print(
    Solution().generateParenthesis(n=3)
)



# ================ Méthode 2 : Backtracking ================

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def backtrack(s : str , n_open : int , n_close : int) : 
            
            if len(s) == n * 2 :
                res.append(s)
                return
            if n_open < n : 
                backtrack(s + '(' , n_open + 1 , n_close)

            if n_close < n_open : 
                backtrack(s + ')' , n_open , n_close + 1)


        backtrack("" , 0 , 0)


        return res 


print(
    Solution().generateParenthesis(n=3)
)

