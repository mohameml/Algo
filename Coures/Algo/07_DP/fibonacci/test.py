import pytest
from main import Fibo


@pytest.fixture
def methods():
    # on retourne les méthodes à tester
    return [
        Fibo.fibo_naive,
        Fibo.fibo_bottom_up,
        Fibo.fibo_optim_bottom_up,
        Fibo.fibo_top_down,
    ]


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
        (9, 55),
        (10, 89),
    ],
)
def test_known_values(n, expected, methods):
    for f in methods:
        assert f(n) == expected, f"{f.__name__}({n}) incorrect"


def test_all_methods_agree_small_range(methods):
    # On reste sur une plage pas trop grande à cause de la version naive
    for n in range(0, 15):
        vals = [f(n) for f in methods]
        assert all(v == vals[0] for v in vals), f"Incohérence pour n={n}: {vals}"


def test_recurrence_holds(methods):
    # Vérifie f(n) = f(n-1) + f(n-2) pour n>=2
    for f in methods:
        for n in range(2, 15):
            assert f(n) == f(n - 1) + f(n - 2), f"Récurrence cassée pour {f.__name__} n={n}"


def test_monotonic_increasing(methods):
    # Avec f0=f1=1, la suite est non décroissante et strictement croissante dès n>=2
    for f in methods:
        prev = f(0)
        for n in range(1, 15):
            cur = f(n)
            assert cur >= prev, f"{f.__name__} n={n} n'est pas monotone"
            prev = cur


def test_fast_methods_large_n():
    # Ici on exclut naive (trop lente) et on vérifie que les 3 autres concordent
    fast = [Fibo.fibo_bottom_up, Fibo.fibo_optim_bottom_up, Fibo.fibo_top_down]
    for n in [20, 30, 50, 100, 300]:
        vals = [f(n) for f in fast]
        assert all(v == vals[0] for v in vals), f"Incohérence fast pour n={n}: {vals}"


