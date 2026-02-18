import pytest

from main import GridTravel


@pytest.mark.parametrize(
    "m,n,expected",
    [
        (0, 0, 0),
        (0, 5, 0),
        (5, 0, 0),
        (1, 1, 1),
        (1, 5, 1),
        (5, 1, 1),
        (2, 2, 2),
        (2, 3, 3),
        (3, 2, 3),
        (3, 3, 6),
        (3, 4, 10),
        (4, 3, 10),
        (4, 4, 20),
        (5, 5, 70),
    ],
)
def test_grid_travel_expected_values(m, n, expected):
    assert GridTravel.solve_top_down(m, n) == expected
    assert GridTravel.solve_bottom_up(m, n) == expected
    assert GridTravel.solve_bottom_up_optim(m, n) == expected


def test_symmetry_property():
    # grid(m, n) == grid(n, m)
    for m in range(0, 8):
        for n in range(0, 8):
            assert GridTravel.solve_top_down(m, n) == GridTravel.solve_top_down(n, m)
            assert GridTravel.solve_bottom_up(m, n) == GridTravel.solve_bottom_up(n, m)
            assert GridTravel.solve_bottom_up_optim(m, n) == GridTravel.solve_bottom_up_optim(n, m)


def test_consistency_between_methods_small_cases():
    # compare all methods on small sizes (naive is exponential)
    for m in range(0, 7):
        for n in range(0, 7):
            naive = GridTravel.solve_naive(m, n)
            topdown = GridTravel.solve_top_down(m, n)
            bottomup = GridTravel.solve_bottom_up(m, n)
            optim = GridTravel.solve_bottom_up_optim(m, n)

            assert naive == topdown == bottomup == optim


def test_large_case_fast_methods_only():
    # bigger grid: naive too slow, so test only efficient methods
    m, n = 18, 18
    td = GridTravel.solve_top_down(m, n)
    bu = GridTravel.solve_bottom_up(m, n)
    opt = GridTravel.solve_bottom_up_optim(m, n)

    assert td == bu == opt


@pytest.mark.parametrize("m,n", [(0, 1), (1, 0), (0, 10), (10, 0)])
def test_zero_dimension_returns_zero(m, n):
    assert GridTravel.solve_top_down(m, n) == 0
    assert GridTravel.solve_bottom_up(m, n) == 0
    assert GridTravel.solve_bottom_up_optim(m, n) == 0
    assert GridTravel.solve_naive(m, n) == 0
