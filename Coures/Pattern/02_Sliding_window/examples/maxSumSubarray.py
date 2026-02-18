def maxSumSubarray(arr , k):

    if len(arr) < k :
        return None 

    somme = sum(arr[:k])
    max_somme = somme
    left = 0 
    
    for right in range(k , len(arr)):
        somme = somme + arr[right] - arr[right - k]
        max_somme = max(somme , max_somme)
    
    return max_somme

# Test 1 : O(n) : somme maximale d'un sous tab de taille k :
arr = [1 , 2 , 4 , 6 , 1 , 7]
k = 2
somme = maxSumSubarray(arr , k) # max_somme = 10 
print(somme)

