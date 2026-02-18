import pytest
from bst import BST


def assert_is_sorted_strict(xs):
    assert xs == sorted(xs)
    assert len(xs) == len(set(xs))


def assert_is_sorted_non_decreasing(xs):
    assert xs == sorted(xs)


# ---------- Fixtures ----------
@pytest.fixture
def bst_basic():
    # arbre classique
    #           8
    #         /   \
    #        3     10
    #       / \      \
    #      1   6      14
    #         / \     /
    #        4   7   13
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    return BST(values)


# ---------- Init / len / inorder ----------
def test_init_empty():
    t = BST()
    assert len(t) == 0
    assert t.inorder() == []


def test_init_iterable_and_inorder_sorted(bst_basic):
    assert len(bst_basic) == 9
    inorder = bst_basic.inorder()
    assert_is_sorted_strict(inorder)
    assert inorder == [1, 3, 4, 6, 7, 8, 10, 13, 14]


def test_iter_matches_inorder(bst_basic):
    assert list(iter(bst_basic)) == bst_basic.inorder()


# ---------- contains / search ----------
@pytest.mark.parametrize("x,expected", [(8, True), (1, True), (13, True), (2, False), (100, False)])
def test_contains(bst_basic, x, expected):
    assert bst_basic.contains(x) is expected


# ---------- min / max ----------
def test_min_max(bst_basic):
    assert bst_basic.min() == 1
    assert bst_basic.max() == 14


def test_min_max_empty_raises():
    t = BST()
    with pytest.raises(ValueError):
        t.min()
    with pytest.raises(ValueError):
        t.max()


# ---------- insert ----------
def test_insert_new_increases_size_and_contains():
    t = BST()
    t.insert(5)
    t.insert(2)
    t.insert(7)
    assert len(t) == 3
    assert t.contains(2)
    assert t.contains(5)
    assert t.contains(7)
    assert t.inorder() == [2, 5, 7]


def test_insert_duplicate_raises_by_default():
    t = BST([5, 2, 7])
    with pytest.raises(ValueError):
        t.insert(5)


def test_insert_duplicate_allowed_when_flag_true():
    t = BST([5, 2, 7], allow_duplicates=True)
    t.insert(5)
    t.insert(5)
    assert len(t) == 5
    inorder = t.inorder()
    # non décroissant (avec doublons)
    assert_is_sorted_non_decreasing(inorder)
    assert inorder.count(5) == 3


# ---------- successor ----------
def test_successor_middle(bst_basic):
    # inorder: [1,3,4,6,7,8,10,13,14]
    assert bst_basic.successor(1) == 3
    assert bst_basic.successor(3) == 4
    assert bst_basic.successor(6) == 7
    assert bst_basic.successor(8) == 10
    assert bst_basic.successor(10) == 13


def test_successor_max_is_none(bst_basic):
    assert bst_basic.successor(14) is None


def test_successor_missing_key_is_none(bst_basic):
    assert bst_basic.successor(999) is None


def test_successor_case_right_subtree_min():
    # cas important : si node a un right, succ = min(right)
    #      20
    #     /  \
    #   10    30
    #        /
    #      25
    t = BST([20, 10, 30, 25])
    assert t.successor(20) == 25
    assert t.successor(25) == 30
    assert t.successor(10) == 20


# ---------- delete ----------
def test_delete_missing_returns_false_no_change(bst_basic):
    before = bst_basic.inorder()
    before_len = len(bst_basic)
    assert bst_basic.delete(999) is False
    assert len(bst_basic) == before_len
    assert bst_basic.inorder() == before


def test_delete_leaf(bst_basic):
    # 4 est une feuille dans cet arbre
    assert bst_basic.delete(4) is True
    assert not bst_basic.contains(4)
    assert len(bst_basic) == 8
    assert_is_sorted_strict(bst_basic.inorder())


def test_delete_node_with_one_child():
    # Construire un cas simple :
    #   5
    #  /
    # 3
    #  \
    #   4
    t = BST([5, 3, 4])
    assert t.delete(3) is True
    assert t.inorder() == [4, 5]
    assert len(t) == 2


def test_delete_node_with_two_children(bst_basic):
    # 3 a deux enfants (1 et 6...) dans bst_basic
    assert bst_basic.delete(3) is True
    assert not bst_basic.contains(3)
    assert len(bst_basic) == 8
    inorder = bst_basic.inorder()
    assert_is_sorted_strict(inorder)
    # 3 doit être absent
    assert 3 not in inorder


def test_delete_root_two_children():
    # root 8 a deux enfants
    t = BST([8, 3, 10, 1, 6, 14, 4, 7, 13])
    assert t.delete(8) is True
    assert len(t) == 8
    inorder = t.inorder()
    assert_is_sorted_strict(inorder)
    assert 8 not in inorder


def test_delete_all_elements():
    t = BST([2, 1, 3])
    assert t.delete(2) is True
    assert t.delete(1) is True
    assert t.delete(3) is True
    assert len(t) == 0
    assert t.inorder() == []
    assert t.root is None


# ---------- delete with duplicates (if you use allow_duplicates=True) ----------
def test_delete_with_duplicates_allowed_removes_one_occurrence():
    t = BST([5, 2, 7, 5, 5], allow_duplicates=True)
    assert len(t) == 5
    assert t.inorder().count(5) == 3

    assert t.delete(5) is True
    assert len(t) == 4
    assert t.inorder().count(5) == 2
    assert_is_sorted_non_decreasing(t.inorder())
