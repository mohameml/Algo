
# PB 2 : Sacs à dos DP2  
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class Item:
    """
    An item that can be chosen in the knapsack.

    Attributes
    ----------
    value : int
        Benefit gained if the item is selected.
    weight : int
        Capacity consumed if the item is selected.
    """
    value: int
    weight: int


@dataclass(frozen=True)
class KnapsackProblem:
    """
    Definition of a 0/1 knapsack problem.

    Attributes
    ----------
    items : List[Item]
        Available items. Each item can be selected at most once (0/1 variant).
    capacity : int
        Maximum total weight allowed in the knapsack.
    """
    items: List[Item]
    capacity: int


@dataclass
class KnapsackSolution:
    """
    Result of solving a knapsack problem.

    Attributes
    ----------
    max_value : int
        Maximum achievable value under the capacity constraint.
    selected_items : List[Item]
        Items chosen in one optimal solution (may not be unique).
    total_weight : int
        Total weight of selected items.
    """
    max_value: int
    selected_items: List[Item]
    total_weight: int


class KnapsackSolver:
    """
    Solver for the 0/1 Knapsack problem (each item can be chosen at most once).

    Problem statement
    -----------------
    Given a capacity C and N items (value_i, weight_i), choose a subset that
    maximizes total value while keeping total weight <= C.

    
    - Bellman equation : 
        - Phi(N , V) = max(u_n + Phi(n-1 , V - v_n) ,Phi(n-1 , V)) with v_n <= V 
        - Phi(N , V) = Phi(N - 1 , V) if v_n > V 
        - Phi(0 , V) = 0


    Bellman recurrence (0/1 knapsack)
    ---------------------------------
    Let dp[i][w] = maximum value using the first i items with capacity w.

    - If weight_i > w:
        dp[i][w] = dp[i-1][w]
    - Else:
        dp[i][w] = max(dp[i-1][w], value_i + dp[i-1][w - weight_i])

    Base:
        dp[0][w] = 0 for all w
    """


    @classmethod
    def solve_naive(cls, problem: KnapsackProblem) -> int:
        
        if problem.capacity == 0 or not problem.items : 
            return 0 
        
        item_n = problem.items[-1]
        rest = problem.items[:-1]
        if item_n.weight <= problem.capacity : 
            take = item_n.value + cls.solve_naive(
                KnapsackProblem(items=rest,capacity=problem.capacity - item_n.weight)
            )
            skip = cls.solve_naive(
                KnapsackProblem(items=rest,capacity=problem.capacity)
            )
            return max(take,skip)
        
        return cls.solve_naive(KnapsackProblem(items=rest,capacity=problem.capacity))

    @classmethod
    def solve_top_down(cls , problem : KnapsackProblem) -> int : 
        
        items = problem.items
        C = problem.capacity 
        N = len(items)

        cache : Dict[Tuple[int,int]  , int] = {}

        def dp(i : int , cap : int) -> int :
            # 1. base case : 
            if i == 0 or cap == 0 : 
                return 0 
            
            # 2. if the input in cache : 
            key = (i , cap)
            if key in cache : 
                return cache[key]
            
            # 3. if it is the first time we calcultae the dp(i,cap): 
            # a. skip : 
            best = dp(i - 1 , cap)


            # b. take : 
            item = items[i - 1]
            if item.weight <= cap : 
                best = max(best , item.value + dp(i - 1 , cap - item.weight))

            # update the cache 
            cache[key] = best 
            return best 
        
        return dp(N,C)

    
    @classmethod
    def solve_bottom_up(cls , problem : KnapsackProblem) -> int : 
        N = len(problem.items)
        C = problem.capacity
        items = problem.items

        dp = [[0]*(C+1) for i in range(N + 1)]

        for i in range(1 , N+1) : 
            item = items[i - 1]
            value = item.value 
            weight = item.weight
            for cap in range(C+1):
                best = dp[i-1][cap]
                if weight <= cap : 
                    best = max(best , value + dp[i - 1][cap - weight])
                dp[i][cap] = best 
        
        return dp[N][C]


    @classmethod
    def solve(cls, problem: KnapsackProblem) -> KnapsackSolution:
        """
        Solve the given 0/1 knapsack problem via dynamic programming and
        reconstruct one optimal selection.

        Complexity
        ----------
        Time  : O(N * C)
        Space : O(N * C) (kept to allow reconstruction)

        Parameters
        ----------
        problem : KnapsackProblem
            Items + capacity.

        Returns
        -------
        KnapsackSolution
            max_value and one optimal set of selected items.
        """
        items = problem.items
        C = problem.capacity
        n = len(items)

        # dp[i][w] = best value using first i items under capacity w
        dp = [[0] * (C + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            v = items[i - 1].value
            wt = items[i - 1].weight
            for w in range(C + 1):
                dp[i][w] = dp[i - 1][w]
                if wt <= w:
                    dp[i][w] = max(dp[i][w], v + dp[i - 1][w - wt])

        # Reconstruct chosen items
        selected: List[Item] = []
        w = C
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                item = items[i - 1]
                selected.append(item)
                w -= item.weight

        
        selected.reverse()
        total_weight = sum(it.weight for it in selected)

        return KnapsackSolution(
            max_value=dp[n][C],
            selected_items=selected,
            total_weight=total_weight
        )
