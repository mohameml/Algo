

def daily_temp(temps : list[int]) -> list[int]:

    stack = [] # (temp , index)
    res = [0 for _ in range(len(temps))]

    for i , t in enumerate(temps) : 
        while stack and t > stack[-1][0]: 
            prev_t , prev_t_index = stack.pop()
            res[prev_t_index] = i - prev_t_index  
        stack.append((t , i))
    
    return res 

print(
    daily_temp([72 , 73 , 74 , 71 , 69 , 79 , 67])
)