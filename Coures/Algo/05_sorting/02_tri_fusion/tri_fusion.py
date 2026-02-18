def merge(l1 : list[int] , l2 : list[int]) -> list[int] : 


    res = []
    i1 = 0 
    i2 = 0 

    while i1 < len(l1) and i2 < len(l2) : 

        if l1[i1] < l2[i2] : 
            res.append(l1[i1])
            i1 += 1
        else : 
            res.append(l2[i2])
            i2 += 1 
    
    res += l1[i1 :]
    res += l2[i2 :]

    return res 


def merge_sort(l  : list[int]) -> list[int] : 

    if len(l) <= 1: 
        return l 

    mid =  len(l) // 2 

    left_sort = merge_sort(l[:mid])
    right_sort = merge_sort(l[mid:]) 
    return merge(left_sort , right_sort)




# Test : 

l = [1,4,2,6,7,3,2]
l_sort = merge_sort(l)
print(l_sort)
