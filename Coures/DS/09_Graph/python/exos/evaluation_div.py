""" 
LeetCode 399 : Evaluate Division

- You are given an array of variable pairs equations and an array of real numbers values, 
- where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

- You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

- Return the answers to all queries. If a single answer cannot be determined, return -1.0.

- Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

- Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

> **Example 1:**

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0


"""

from collections import deque
from typing import List , Optional , Dict , Tuple 

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph : Dict[str , List[str]] = {}
        w : Dict[Tuple[str ,str] , float] = {}

        for (x,y),val in zip(equations,values) : 
            graph.setdefault(x,[]).append(y)
            graph.setdefault(y,[]).append(x)
            w[(x,y)] = val
            w[(y,x)] = 1.0 / val 
        
        def spath(start : str , end : str) -> Optional[list[str]] :

            if start == end : 
                return [start]

            queue = deque([(start , [start])])
            visited = {start}

            while queue : 
                curr , path = queue.popleft()
                for neighbor in graph.get(curr , []) : 
                    if neighbor not in visited : 
                        visited.add(neighbor)
                        new_path = path + [neighbor]
                        if neighbor == end : 
                            return new_path 
                        queue.append((neighbor , new_path))

            return None 

        res = []        
        for start,end in queries :
            if start not in graph or end not in graph : 
                res.append(-1.0)
                continue 
        
            path = spath(start , end)
            if not path : 
                res.append(-1)
                continue 

            q_val = 1.0
            for a,b in zip(path,path[1:]) : 
                q_val *= w[(a,b)]
            res.append(q_val)
        
        return res 

