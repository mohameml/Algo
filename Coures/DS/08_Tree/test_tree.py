from __future__ import annotations 
from typing import Callable , Iterable , Any 
import time 
import traceback
from tree import TreeNode

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"


def run_functions(funcs: Iterable[Callable[[], Any]], *, stop_on_fail: bool = False) -> dict:
    """
    Exécute une liste de fonctions (sans arguments).
    Affiche un log coloré + un récap final.
    
    Params:
      - funcs: itérable de fonctions (callables) sans args
      - stop_on_fail: si True, stop au premier échec

    Retourne un dict de stats.
    """
    funcs = list(funcs)
    total = len(funcs)
    ok = 0
    fail = 0
    results = []  # liste de dicts {name, status, duration_ms, error?}

    start_all = time.perf_counter()

    for idx, fn in enumerate(funcs, start=1):
        name = getattr(fn, "__name__", str(fn))
        print(f"{CYAN}{BOLD}==== {name} ({idx}/{total}) ===={RESET}")

        start = time.perf_counter()
        try:
            fn()
            duration_ms = (time.perf_counter() - start) * 1000
            ok += 1
            print(f"status {name} : {GREEN}{BOLD}OK{RESET}  ({duration_ms:.1f} ms)\n")
            results.append({"name": name, "status": "OK", "duration_ms": duration_ms})
        except Exception as e:
            duration_ms = (time.perf_counter() - start) * 1000
            fail += 1
            print(f"status {name} : {RED}{BOLD}FAIL{RESET} ({duration_ms:.1f} ms)")
            print(f"{YELLOW}Exception: {type(e).__name__}: {e}{RESET}")
            # stack trace pour debug (tu peux l'enlever si tu veux)
            traceback.print_exc()
            print()
            results.append({
                "name": name,
                "status": "FAIL",
                "duration_ms": duration_ms,
                "error": f"{type(e).__name__}: {e}",
            })
            if stop_on_fail:
                break

    total_ms = (time.perf_counter() - start_all) * 1000

    # --- Récap final ---
    print(f"{BOLD}===== STATS ====={RESET}")
    print(f"Total   : {total}")
    print(f"{GREEN}OK      : {ok}{RESET}")
    print(f"{RED}FAIL    : {fail}{RESET}")
    print(f"Time    : {total_ms:.1f} ms")

    return {
        "total": total,
        "ok": ok,
        "fail": fail,
        "time_ms": total_ms,
        "details": results,
    }








def test_print() : 
    tree = TreeNode(
        1,
        TreeNode(
            2 , 
            TreeNode(4),
            TreeNode(5)
        ),
        TreeNode(3)
    )


    tree.print()

def test_height_of_tree():

    tree = TreeNode(
        1,
        TreeNode(
            2 , 
            TreeNode(4),
            TreeNode(5)
        ),
        TreeNode(3)
    )

    hei_ = tree.height()

    print(f"the height of tree is {hei_}")

    assert hei_ == 3 

def test_is_leaf() : 

    # sub_test 1 : 
    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(4),
                TreeNode(5)
            ),
            TreeNode(3)
    )

    print(f"tree is a leaf tree: {tree.is_leaf()}")

    assert tree.is_leaf() == False 

    # sub_test 2 : 
    print(f"TreeNode(1) is leaf : {TreeNode(1).is_leaf()}")
    assert TreeNode(1).is_leaf() == True 


def test_is_same():
    # sub_test 1 : 
    tree1 = TreeNode(1 , TreeNode(2) , TreeNode(3))
    tree2 = TreeNode(1 , TreeNode(2) , TreeNode(3))

    print(f"tree1 is same as tree2 : {tree1.is_same(tree2)}")

    assert tree1.is_same(tree2) == True 
    # sub_test 2 : 
    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(4),
                TreeNode(5)
            ),
            TreeNode(3)
    )
    print(f"tree1 is not the same as tree : {tree1.is_same(tree)}")
    assert tree1.is_same(tree) == False  


def test_df_rec_preorder(): 
    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(4),
                TreeNode(5)
            ),
            TreeNode(3)
    )
    expected = [1,2,4,5,3]
    vals = tree.dfs(methode_type="rec",dfs_type="preorder")
    print(f"vals : {vals}")

    assert vals == expected

def test_df_rec_inorder(): 
    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(4),
                TreeNode(5)
            ),
            TreeNode(3)
    )
    expected = [4,2,5,1,3]
    vals = tree.dfs(methode_type="rec",dfs_type="inorder")
    print(f"vals : {vals}")

    assert vals == expected


def test_df_rec_postorder(): 
    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(4),
                TreeNode(5)
            ),
            TreeNode(3)
    )
    expected = [4,5,2,3,1]
    vals = tree.dfs(methode_type="rec",dfs_type="postorder")
    print(f"vals : {vals}")

    assert vals == expected


def test_df_iter_preorder(): 
    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(4),
                TreeNode(5)
            ),
            TreeNode(3)
    )
    expected = [1,2,4,5,3]
    vals = tree.dfs(methode_type="iter",dfs_type="preorder")
    print(f"vals : {vals}")

    assert vals == expected


def test_df_iter_inorder(): 
    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(4),
                TreeNode(5)
            ),
            TreeNode(3)
    )
    expected = [4,2,5,1,3]
    vals = tree.dfs(methode_type="iter",dfs_type="inorder")
    print(f"vals : {vals}")

    assert vals == expected


def test_df_iter_postorder(): 
    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(4),
                TreeNode(5)
            ),
            TreeNode(3)
    )

    expected = [4,5,2,3,1]
    vals = tree.dfs(methode_type="iter",dfs_type="postorder")
    print(f"vals : {vals}")

    assert vals == expected

def test_get_leaf_values():

    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(4),
                TreeNode(5)
            ),
            TreeNode(3)
    )

    exc_ = [4,5,3]

    leaf_values = tree.get_leaf_values()

    print(f"leaf_values : {leaf_values}")


    assert leaf_values == exc_ 

def test_get_sum_per_path():

    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(3),
                TreeNode(1)
            ),
            TreeNode(
                4,
                TreeNode(5)
            )
    )

    exc_ = [6,4,10]

    sum_per_path = tree.get_sum_per_path()

    print(f"sum per path of tree is {sum_per_path}")

    assert sum_per_path == exc_ 





def test_is_valid_BST(): 
    tree = TreeNode(
        10,
        TreeNode(
            5,
            TreeNode(
                3,
                TreeNode(1)
            ),
        ),
        TreeNode(
            12,
            None,
            TreeNode(14)

        )
    )
    tree.print()
    is_valid = tree.is_valide_bst()

    print(f"is valide BST : {is_valid}")

    assert is_valid == True 


    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(3),
                TreeNode(1)
            ),
            TreeNode(
                4,
                TreeNode(5)
            )
    )

    tree.print()
    is_valid = tree.is_valide_bst()

    print(f"is valide BST : {is_valid}")

    assert is_valid == False 


def test_bfs_level_order() : 

    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(3),
                TreeNode(1)
            ),
            TreeNode(
                4,
                TreeNode(5)
            )
    )

    tree.print()

    exc_ = [1 , 2 , 4 , 3, 1 , 5]
    bfs_order = tree.bfs_level_order()

    print(f"BFS level order : {bfs_order}")

    assert bfs_order == exc_


def test_bfs_levels() : 

    tree = TreeNode(
            1,
            TreeNode(
                2 , 
                TreeNode(3),
                TreeNode(1)
            ),
            TreeNode(
                4,
                TreeNode(5)
            )
    )


    exc_ = [[1] , [2 , 4] , [3, 1 , 5]]
    bfs_order = tree.bfs_levels()

    print(f"BFS levels : {bfs_order}")

    assert bfs_order == exc_




if __name__ == "__main__":
    tests = [
        test_print,
        test_height_of_tree,
        test_is_leaf,
        test_is_same,
        test_df_rec_preorder,
        test_df_rec_inorder,
        test_df_rec_postorder,
        test_df_iter_preorder,
        test_df_iter_inorder,
        test_df_iter_postorder,
        test_get_leaf_values,
        test_get_sum_per_path ,
        test_is_valid_BST,
        test_bfs_level_order ,
        test_bfs_levels, 
    ]

    run_functions(tests)