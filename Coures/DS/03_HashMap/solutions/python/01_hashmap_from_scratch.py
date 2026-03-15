"""
Exo 1 : HashMap from scratch
---------------------------------
Implémenter un HashMap avec chaining (liste chaînée par bucket).
Opérations : put(key, value), get(key), remove(key), contains(key).
Resize automatique quand load factor > 0.7.

Examples :
---------------
hm = HashMap()
hm.put("a", 1)
hm.get("a") => 1
hm.contains("a") => True
hm.remove("a")
hm.contains("a") => False

----
times : 0
last_date :
"""


class HashMap:

    def __init__(self, capacity=16):
        self._capacity = capacity
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]

    def _hash(self, key):
        return hash(key) % self._capacity

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

        if self._size / self._capacity > 0.7:
            self._resize()

    def get(self, key):
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return v
        raise KeyError(key)

    def contains(self, key):
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return True
        return False

    def __len__(self):
        return self._size

    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def __repr__(self):
        items = []
        for bucket in self._buckets:
            for k, v in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"


if __name__ == "__main__":

    # Test 1 : put + get
    hm = HashMap()
    hm.put("a", 1)
    hm.put("b", 2)
    assert hm.get("a") == 1
    assert hm.get("b") == 2

    # Test 2 : update existing key
    hm.put("a", 10)
    assert hm.get("a") == 10

    # Test 3 : contains
    assert hm.contains("a") == True
    assert hm.contains("z") == False

    # Test 4 : remove
    hm.remove("a")
    assert hm.contains("a") == False
    assert len(hm) == 1

    # Test 5 : KeyError
    try:
        hm.get("missing")
        assert False
    except KeyError:
        pass

    # Test 6 : resize (many inserts)
    hm2 = HashMap()
    for i in range(100):
        hm2.put(f"key_{i}", i)
    assert len(hm2) == 100
    assert hm2.get("key_50") == 50

    print("All tests passed!")
