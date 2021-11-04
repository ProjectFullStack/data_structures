"""
hash_table_with_separate_chaining.py
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
        if self._map[insert_index] is None:
            self._map[insert_index] = []

        # iterate over the keys in this list and check if the key exists
        # if so, update it
        # else append it
        for i in range(len(self._map[insert_index])):
            if self._map[insert_index][i][0] == key:
                # update
                self._map[insert_index][i][1] = val
                return

        self._map[insert_index].append([key, val])

    def get(self, key):
        lookup_index = self._hash(key)
        if self._map[lookup_index] is not None:
            for k, v in self._map[lookup_index]:
                if k == key:
                    return v

    def keys(self):
        key_store = []
        for bucket in self._map:
            if bucket is not None:
                for k, v in bucket:
                    key_store.append(k)
        return key_store
