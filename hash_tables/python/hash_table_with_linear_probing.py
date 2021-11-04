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
        hash_index = len(key) % self.size
        return hash_index

    def _increment_key(self, key):
        return (key + 1) % self.size

    def print_table(self):
        for i,val in enumerate(self._map):
            print(i, ": ", val)

    def set(self, key, val):
        insert_index = self._hash(key)

        if self._map[insert_index] is not None:

            # check if the key exists at insert index, that is we are inserting
            # the same key, or trying to update it
            if self._map[insert_index][0] == key:
                self._map[insert_index][1] = val
                return

            # otherwise, start probing to the right
            exit_index = insert_index
            while self._map[insert_index] != None and self._map[insert_index][0] != key:
                insert_index = self._increment_key(insert_index)
                if insert_index == exit_index:
                    raise KeyError("This hash table has reached it's max keys")

        self._map[insert_index] = [key, val]

    def get(self, key):
        lookup_index = self._hash(key)

        if self._map[lookup_index][0] != key:
            exit_index = lookup_index
            while self._map[lookup_index] != None and self._map[lookup_index][0] != key:
                lookup_index = self._increment_key(lookup_index)
                if lookup_index == exit_index:
                    raise KeyError(f"Key {key} not found")

        if self._map[lookup_index] is None:
            raise KeyError(f"Key {key} not found")
        return self._map[lookup_index][1]

    def keys(self):
        key_store = []
        for bucket in self._map:
            if bucket is not None:
                for k, v in bucket:
                    key_store.append(k)
        return key_store




if __name__ == "__main__":
    ht = HashTable()
    ht.set("Jon", '1 Main St')
