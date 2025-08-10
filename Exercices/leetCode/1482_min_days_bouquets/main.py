# f = [1 , 1 , 0 , 0 , 1 ]
#Q :  est ce que t'a K 1 consécutives 
from typing import Callable , List 


# def is_k_cons(f : list[int] , k : int) -> bool : 

#     count = 0 

#     for val in f : 
#         if val == 1 : 
#             count += 1
#             if count >= k :
#                 return True 
#         else : 
#             count = 0 
    
#     return False

# def can_make_m_bouquets(flowers : list[int] , k : int , m : int) -> bool : 

#     count = 0 
#     m_ = 0 

#     for val in flowers :

#         if val == 1 : 
#             count += 1

#             if count == k : 
#                 m_ += 1
#                 count = 0 
#         else : 
#             count = 0

#     return m_ >= m 



def minDays(bloomDay: List[int], m: int, k: int) -> int:
    
    if m * k > len(bloomDay) : 
        return -1 


    def can_make_m_bouquets(day : int ) -> bool : 

        count = 0 
        bouquets = 0 

        for  bloom in bloomDay : 

            if bloom <= day : 
                count += 1 

                if count == k : 
                    bouquets += 1
                    count = 0 
            
            else : 
                count = 0 

        return bouquets >= m 


    low = min(bloomDay)
    high = max(bloomDay)

    while low < high : 

        mid = (low + high) // 2

        if can_make_m_bouquets(mid) : 
            high = mid 
        else : 
            low = mid +  1
    
    return low 



bloomDay = [1,10,3,10,2]
m = 3
k = 1

min_d = minDays(bloomDay , m , k)
print(f"the min days is : {min_d}")
