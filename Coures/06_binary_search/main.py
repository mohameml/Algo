"""
def binary_search_general(nums, phi, C):
    \"""
    Trouve le plus petit index j tel que phi(nums[j]) <= C.
    nums doit être trié.
    phi : fonction monotone (croissante ou décroissante)
    \"""
    left, right = 0, len(nums) - 1
    result = -1  # ou None si tu veux

    while left <= right:
        mid = (left + right) // 2
        if phi(nums[mid]) <= C:
            result = mid  # possible candidat
            right = mid - 1  # on cherche plus petit encore
        else:
            left = mid + 1  # trop petit, on monte
    return result

"""


def binary_search_general(
    nums : list[int],
    phi : callable,
    C : int 
) : 
    """
    Trouve le plus petit index j tel que phi(nums[j]) <= C.
    nums doit être trié.
    phi : fonction monotone (croissante ou décroissante)
    """
    left = 0 
    right = len(nums) - 1
    res = 0 

    while left <= right : 
        
        mid = left + right // 2     

        if phi(nums[mid]) <= C : 
            res = mid 
            right = mid 
        else :
            left = mid + 1

    return None 