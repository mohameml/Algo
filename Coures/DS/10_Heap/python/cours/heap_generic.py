from typing import TypeVar, Generic, List, Callable, Optional
from dataclasses import dataclass

T = TypeVar('T')  # type générique — peut être int, tuple, objet, etc.

class Heap(Generic[T]):
    """
    Heap générique qui accepte n'importe quel type T.

    Le comportement Min/Max est contrôlé par le comparateur :
        comparator(a, b) retourne True si a DOIT être au-dessus de b

    Exemples :
        Min-Heap entiers  → comparator = lambda a, b: a < b
        Max-Heap entiers  → comparator = lambda a, b: a > b
        Min-Heap tuples   → comparator = lambda a, b: a[0] < b[0]
    """

    def __init__(self, comparator: Callable[[T, T], bool]) -> None:
        self._data:       List[T]            = []
        self._comparator: Callable[[T, T], bool] = comparator

    # ─────────────────────────────────────────────
    # HELPERS
    # ─────────────────────────────────────────────

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _has_parent(self, i: int) -> bool:
        return i > 0

    def _has_left(self, i: int) -> bool:
        return self._left(i) < len(self._data)

    def _has_right(self, i: int) -> bool:
        return self._right(i) < len(self._data)

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _has_priority(self, i: int, j: int) -> bool:
        """
        Retourne True si l'élément à l'index i
        doit être AU-DESSUS de l'élément à l'index j.
        Délègue entièrement au comparateur.
        """
        return self._comparator(self._data[i], self._data[j])

    # ─────────────────────────────────────────────
    # LECTURE
    # ─────────────────────────────────────────────

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self._data[0]

    def size(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    # ─────────────────────────────────────────────
    # INSERT — O(log n)
    # ─────────────────────────────────────────────

    def insert(self, val: T) -> None:
        self._data.append(val)
        self._heapify_up(len(self._data) - 1)

    def _heapify_up(self, i: int) -> None:
        while self._has_parent(i):
            p = self._parent(i)
            if self._has_priority(i, p):   # i doit être au-dessus de son parent ?
                self._swap(i, p)
                i = p
            else:
                break

    # ─────────────────────────────────────────────
    # EXTRACT — O(log n)
    # ─────────────────────────────────────────────

    def extract(self) -> T:
        if self.is_empty():
            raise IndexError("Heap is empty")

        top: T = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()

        if not self.is_empty():
            self._heapify_down(0)

        return top

    def _heapify_down(self, i: int) -> None:
        while self._has_left(i):
            # trouve l'enfant avec la plus haute priorité
            priority_child: int = self._left(i)

            if self._has_right(i) and self._has_priority(self._right(i), priority_child):
                priority_child = self._right(i)

            if self._has_priority(priority_child, i):   # l'enfant doit être au-dessus ?
                self._swap(i, priority_child)
                i = priority_child
            else:
                break

    # ─────────────────────────────────────────────
    # BUILD HEAP — O(n)
    # ─────────────────────────────────────────────

    @classmethod
    def from_list(cls, values: List[T], comparator: Callable[[T, T], bool]) -> "Heap[T]":
        heap: Heap[T]  = cls(comparator)
        heap._data     = list(values)
        n: int         = len(heap._data)

        for i in range((n - 2) // 2, -1, -1):
            heap._heapify_down(i)

        return heap

    def __repr__(self) -> str:
        return f"Heap({self._data})"


## Usage 1 : 
min_heap : Heap[int] = Heap(comparator=lambda a ,b: a < b)
min_heap.insert(5)
min_heap.insert(2)
min_heap.insert(8)
print(min_heap.peek())

## Usage 2 : 
max_heap : Heap[int] = Heap(comparator=lambda a,b : a >b)
max_heap.insert(5)
max_heap.insert(2)
max_heap.insert(8)
print(max_heap.peek())


## Usage 3 : Heap of tuples 
graph_heap : Heap[tuple[int , str]] = Heap(
    comparator=lambda a,b : a[0] < b [0]
)

graph_heap.insert((5,'A'))
graph_heap.insert((1,'B'))
graph_heap.insert((3,'C'))

print(graph_heap.extract())
print(graph_heap.extract())
print(graph_heap.extract())

## Usgae 4  : Heap of custom object 
@dataclass
class Task : 
    priority : int 
    name : str 

    def __repr__(self) -> str:
        return f"Task(priority={self.priority},name='{self.name}')"

task_heap : Heap[Task] = Heap(
    comparator=lambda a,b : a.priority < b.priority
)

task_heap.insert(Task(priority=3,name="Send email"))
task_heap.insert(Task(priority=1,name="Fix prod bug"))
task_heap.insert(Task(priority=2,name="Code review"))

print(task_heap.extract())
print(task_heap.extract())
print(task_heap.extract())


