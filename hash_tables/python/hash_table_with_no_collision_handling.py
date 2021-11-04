"""
hash_table_with_no_collision_handling.py
ProjectFullStack
20211103
"""

class HashTable:

    def __init__(self, size=9):
        self.size = size
        self._map = [None] * self.size

    def _hash(self, key):
        return len(key) % self.size

    def print_table(self):
        for i,val in enumerate(self._map):
            print(i, ": ", val)

    def set(self, key, val):
        insert_index = self._hash(key)
        self._map[insert_index] = [key, val]

    def get(self, key):
        lookup_index = self._hash(key)
        if self._map[lookup_index] is None:
            return None
        if self._map[lookup_index][0] == key:
            return self._map[lookup_index][1]
        return None

    def keys(self):
        key_store = []
        for bucket in self._map:
            if bucket is not None:
                key_store.append(bucket[0])
        return key_store




if __name__ == "__main__":
    ht = HashTable()
    ht.set("Jon", '1 Main St')
    ht.set("Mike", '13 South St')
    ht.set("Amy", '98 Cherry St')
    ht.print_table()
    print(ht.keys())
    print(ht.get("Amy"))
    print(ht.get("Jon"))
