import time
import pytest
from main import Item, KnapsackProblem, KnapsackSolver , KnapsackSolution


def test_empty_items():
    problem = KnapsackProblem(items=[], capacity=10)
    assert KnapsackSolver.solve_naive(problem) == 0


def test_zero_capacity():
    items = [Item(value=10, weight=5)]
    problem = KnapsackProblem(items=items, capacity=0)
    assert KnapsackSolver.solve_naive(problem) == 0


def test_single_item_fits():
    items = [Item(value=10, weight=5)]
    problem = KnapsackProblem(items=items, capacity=5)
    assert KnapsackSolver.solve_naive(problem) == 10


def test_single_item_does_not_fit():
    items = [Item(value=10, weight=6)]
    problem = KnapsackProblem(items=items, capacity=5)
    assert KnapsackSolver.solve_naive(problem) == 0


def test_two_items_choose_best():
    items = [
        Item(value=10, weight=5),
        Item(value=7, weight=3),
    ]
    problem = KnapsackProblem(items=items, capacity=5)
    # mieux de prendre l'objet (7,3) que (10,5) ? NON → 10 > 7
    assert KnapsackSolver.solve_naive(problem) == 10


def test_two_items_both_fit():
    items = [
        Item(value=10, weight=5),
        Item(value=7, weight=3),
    ]
    problem = KnapsackProblem(items=items, capacity=8)
    assert KnapsackSolver.solve_naive(problem) == 17


def test_classic_example():
    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=5, weight=4),
    ]
    problem = KnapsackProblem(items=items, capacity=5)
    # meilleure solution : items (3,2) + (4,3) = 7
    assert KnapsackSolver.solve_naive(problem) == 7


def test_order_does_not_matter():
    items1 = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=5, weight=4),
    ]
    items2 = list(reversed(items1))

    p1 = KnapsackProblem(items=items1, capacity=5)
    p2 = KnapsackProblem(items=items2, capacity=5)

    assert KnapsackSolver.solve_naive(p1) == KnapsackSolver.solve_naive(p2)



@pytest.mark.parametrize(
    "items,cap,expected",
    [
        ([], 10, 0),
        ([Item(value=10, weight=5)], 0, 0),
        ([Item(value=10, weight=5)], 5, 10),
        ([Item(value=10, weight=6)], 5, 0),
        ([Item(value=3, weight=2), Item(value=4, weight=3), Item(value=5, weight=4)], 5, 7),
        ([Item(value=6, weight=1), Item(value=10, weight=2), Item(value=12, weight=3)], 5, 22),  # 10+12
    ],
)
def test_top_down_known_cases(items, cap, expected):
    p = KnapsackProblem(items=items, capacity=cap)
    assert KnapsackSolver.solve_top_down(p) == expected


def test_top_down_matches_naive_small():
    # petit cas (naive explose vite)
    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=8, weight=4),
        Item(value=8, weight=5),
        Item(value=10, weight=9),
    ]
    cap = 10
    p = KnapsackProblem(items=items, capacity=cap)

    naive = KnapsackSolver.solve_naive(p)
    topdown = KnapsackSolver.solve_top_down(p)

    assert topdown == naive


def test_order_invariance():
    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=5, weight=4),
        Item(value=6, weight=5),
    ]
    cap = 8
    p1 = KnapsackProblem(items=items, capacity=cap)
    p2 = KnapsackProblem(items=list(reversed(items)), capacity=cap)

    assert KnapsackSolver.solve_top_down(p1) == KnapsackSolver.solve_top_down(p2)



def test_top_down_is_faster_than_naive():
    """
    Compare le temps d'exécution entre la version naïve
    et la version top-down memo.

    Ce test ne cherche pas une précision absolue,
    mais vérifie que le top-down est STRICTEMENT plus rapide.
    """

    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=5, weight=4),
        Item(value=6, weight=5),
        Item(value=7, weight=6),
        Item(value=8, weight=7),
        Item(value=9, weight=8),
        Item(value=10, weight=9),
    ]
    capacity = 15
    problem = KnapsackProblem(items=items, capacity=capacity)

    # --- naive ---
    start = time.perf_counter()
    naive_res = KnapsackSolver.solve_naive(problem)
    naive_time = time.perf_counter() - start

    # --- top-down ---
    start = time.perf_counter()
    topdown_res = KnapsackSolver.solve_top_down(problem)
    topdown_time = time.perf_counter() - start

    # résultats identiques
    assert naive_res == topdown_res

    # top-down doit être plus rapide
    assert topdown_time < naive_time, (
        f"Top-down slower than naive: "
        f"naive={naive_time:.6f}s, topdown={topdown_time:.6f}s"
    )

    print(
        f"\nNaive     : {naive_time:.6f}s"
        f"\nTop-down  : {topdown_time:.6f}s"
        f"\nSpeed-up  : x{naive_time / topdown_time:.1f}"
    )



@pytest.mark.parametrize(
    "items,capacity,expected",
    [
        ([], 10, 0),
        ([Item(value=10, weight=5)], 0, 0),
        ([Item(value=10, weight=5)], 5, 10),
        ([Item(value=10, weight=6)], 5, 0),

        # Exemple classique : (3,2) + (4,3) = 7 sous cap=5
        ([Item(value=3, weight=2), Item(value=4, weight=3), Item(value=5, weight=4)], 5, 7),

        # Cas où le meilleur n'est pas l'objet le plus "value"
        # cap=5, meilleur = 10 (objet poids=5), pas 7 (poids=3)
        ([Item(value=10, weight=5), Item(value=7, weight=3)], 5, 10),

        # Les deux peuvent rentrer (cap=8) -> 17
        ([Item(value=10, weight=5), Item(value=7, weight=3)], 8, 17),

        # Cas standard souvent utilisé : meilleur = 22 (10+12) sous cap=5
        ([Item(value=6, weight=1), Item(value=10, weight=2), Item(value=12, weight=3)], 5, 22),
    ],
)
def test_bottom_up_known_cases(items, capacity, expected):
    problem = KnapsackProblem(items=items, capacity=capacity)
    assert KnapsackSolver.solve_bottom_up(problem) == expected


def test_bottom_up_order_invariant():
    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=5, weight=4),
        Item(value=6, weight=5),
    ]
    cap = 8

    p1 = KnapsackProblem(items=items, capacity=cap)
    p2 = KnapsackProblem(items=list(reversed(items)), capacity=cap)

    assert KnapsackSolver.solve_bottom_up(p1) == KnapsackSolver.solve_bottom_up(p2)


def test_bottom_up_capacity_monotonicity():
    """
    Si la capacité augmente, la valeur optimale ne peut pas diminuer.
    """
    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=8, weight=4),
    ]

    prev = 0
    for cap in range(0, 11):
        p = KnapsackProblem(items=items, capacity=cap)
        cur = KnapsackSolver.solve_bottom_up(p)
        assert cur >= prev
        prev = cur


def test_bottom_up_matches_top_down_small_if_available():
    """
    Optionnel : si tu as solve_top_down, compare les résultats.
    (Ça valide que DP bottom-up et memo top-down font la même chose.)
    """
    if not hasattr(KnapsackSolver, "solve_top_down"):
        pytest.skip("solve_top_down not implemented")

    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=8, weight=4),
        Item(value=8, weight=5),
        Item(value=10, weight=9),
    ]
    cap = 10
    p = KnapsackProblem(items=items, capacity=cap)

    assert KnapsackSolver.solve_bottom_up(p) == KnapsackSolver.solve_top_down(p)


def test_bottom_up_matches_naive_tiny_if_available():
    """
    Optionnel : si tu as solve_naive, compare sur un cas très petit,
    car naive explose vite.
    """
    if not hasattr(KnapsackSolver, "solve_naive"):
        pytest.skip("solve_naive not implemented")

    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=5, weight=4),
        Item(value=6, weight=5),
    ]
    cap = 7
    p = KnapsackProblem(items=items, capacity=cap)

    assert KnapsackSolver.solve_bottom_up(p) == KnapsackSolver.solve_naive(p)


def assert_solution_valid(problem: KnapsackProblem, sol: KnapsackSolution) -> None:
    # 1) total_weight cohérent avec selected_items
    assert sol.total_weight == sum(it.weight for it in sol.selected_items)

    # 2) respecte la capacité
    assert sol.total_weight <= problem.capacity

    # 3) les items sélectionnés proviennent bien de la liste (0/1)
    # (on vérifie par identité d'objet si tu réutilises les mêmes instances)
    for it in sol.selected_items:
        assert it in problem.items

    # 4) max_value cohérent avec selected_items
    assert sol.max_value == sum(it.value for it in sol.selected_items)


@pytest.mark.parametrize(
    "items,cap,expected_value,expected_weight,expected_one_of_sets",
    [
        # Vide
        ([], 10, 0, 0, [set()]),

        # Capacité 0
        ([Item(value=10, weight=5)], 0, 0, 0, [set()]),

        # 1 item qui rentre
        ([Item(value=10, weight=5)], 5, 10, 5, [ {0} ]),

        # 1 item qui ne rentre pas
        ([Item(value=10, weight=6)], 5, 0, 0, [set()]),

        # Exemple classique (3,2)+(4,3)=7 sous cap=5
        (
            [Item(value=3, weight=2), Item(value=4, weight=3), Item(value=5, weight=4)],
            5,
            7,
            5,
            [ {0,1} ]  # indices attendus
        ),

        # Deux items, cap=5 : on prend le meilleur (10,5)
        (
            [Item(value=10, weight=5), Item(value=7, weight=3)],
            5,
            10,
            5,
            [ {0} ]
        ),

        # Deux items, cap=8 : on prend les deux -> 17
        (
            [Item(value=10, weight=5), Item(value=7, weight=3)],
            8,
            17,
            8,
            [ {0,1} ]
        ),

        # Cas connu : meilleur = 22 (10+12) sous cap=5
        (
            [Item(value=6, weight=1), Item(value=10, weight=2), Item(value=12, weight=3)],
            5,
            22,
            5,
            [ {1,2} ]
        ),
    ],
)
def test_solve_known_cases(items, cap, expected_value, expected_weight, expected_one_of_sets):
    problem = KnapsackProblem(items=items, capacity=cap)
    sol = KnapsackSolver.solve(problem)

    assert_solution_valid(problem, sol)
    assert sol.max_value == expected_value
    assert sol.total_weight == expected_weight

    # Vérifier que la sélection correspond à une solution acceptable (pas toujours unique)
    chosen_indices = {problem.items.index(it) for it in sol.selected_items} if items else set()
    assert chosen_indices in expected_one_of_sets


def test_solve_order_invariant_value():
    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=5, weight=4),
        Item(value=6, weight=5),
    ]
    cap = 8

    p1 = KnapsackProblem(items=items, capacity=cap)
    p2 = KnapsackProblem(items=list(reversed(items)), capacity=cap)

    sol1 = KnapsackSolver.solve(p1)
    sol2 = KnapsackSolver.solve(p2)

    assert sol1.max_value == sol2.max_value
    assert sol1.total_weight <= cap
    assert sol2.total_weight <= cap


def test_solve_capacity_monotonicity_value():
    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=8, weight=4),
        Item(value=8, weight=5),
    ]

    prev = 0
    for cap in range(0, 16):
        p = KnapsackProblem(items=items, capacity=cap)
        sol = KnapsackSolver.solve(p)
        assert_solution_valid(p, sol)
        assert sol.max_value >= prev
        prev = sol.max_value


def test_solve_matches_bottom_up_value_if_available():
    # optionnel : si tu as une méthode solve_bottom_up qui renvoie juste la valeur
    if not hasattr(KnapsackSolver, "solve_bottom_up"):
        pytest.skip("solve_bottom_up not implemented")
    items = [
        Item(value=3, weight=2),
        Item(value=4, weight=3),
        Item(value=8, weight=4),
        Item(value=8, weight=5),
        Item(value=10, weight=9),
    ]
    cap = 10
    p = KnapsackProblem(items=items, capacity=cap)
    sol = KnapsackSolver.solve(p)
    val = KnapsackSolver.solve_bottom_up(p)
    assert sol.max_value == val
