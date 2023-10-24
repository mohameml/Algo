#!/usr/bin/env python3




def ceoff_binome_naive_memo(n,p):


    # dict 
    dict_b = {}


    def binome_memo(n,p):

        if (n,p) in dict_b :

            return dict_b[(n,p)]
        
        elif  p==0 or p==n :
            dict_b[(n,p)] = 1
            return 1 

        else :
            res =  binome_memo(n-1,p) + binome_memo(n-1 , p-1)

            dict_b[(n,p)] = res

            return res 

    return binome_memo(n,p)


# test :

n = 100
p = 20
print(f"C({n},{p}) = {ceoff_binome_naive_memo(n,p)}")  