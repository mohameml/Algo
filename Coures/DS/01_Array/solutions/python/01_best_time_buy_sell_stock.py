"""
Exo 2 : Best Time to Buy and Sell Stock
---------------------------------
On a un tableau prices où prices[i] est le prix d'un actif au jour i.
Trouver le profit maximum en achetant puis vendant (une seule transaction).
Si aucun profit possible, retourner 0.

Examples :
---------------
prices = [7, 1, 5, 3, 6, 4] => 5 (acheter à 1, vendre à 6)
prices = [7, 6, 4, 3, 1] => 0 (prix décroissant, aucun profit)


"""

from typing import List


def max_profit(prices: List[int]) -> float | int:
    min_price = float('inf')
    max_prof = 0

    for price in prices:
        min_price = min(min_price, price)
        max_prof = max(max_prof, price - min_price)

    return max_prof


if __name__ == "__main__":

    # Test 1 :
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5

    # Test 2 :
    assert max_profit([7, 6, 4, 3, 1]) == 0

    # Test 3 :
    assert max_profit([2, 4, 1]) == 2

    print("All tests passed!")
