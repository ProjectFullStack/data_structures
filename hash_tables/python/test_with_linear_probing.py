import unittest
from hash_table_with_linear_probing import HashTable


class TestWithLinearProbing(unittest.TestCase):

    def test_init(self):
        """
        Test new Node initialization
        """
        ht = HashTable(size=3)
        self.assertIsInstance(ht, HashTable)
        self.assertEqual(ht.size, 3)
        self.assertEqual(ht._map, [None] * 3)

    def test_hash(self):
        ht = HashTable(size=3)
        self.assertEqual(ht._hash('jon'), 0)
        self.assertEqual(ht._hash('amy'), 0)
        self.assertEqual(ht._hash('lon'), 0)

    def test_set(self):
        ht = HashTable(size=3)
        ht.set('jon', 'jons value')
        self.assertEqual(ht._map[0], ['jon', 'jons value'])
        ht.set('amy', 'amys value')
        self.assertEqual(ht._map[1], ['amy', 'amys value'])
        ht.set('lon', 'lons value')
        self.assertEqual(ht._map[2], ['lon', 'lons value'])
        # inserting another should raise a KeyError
        self.assertRaises(KeyError, ht.set, 'ron', 'rons val')

    def test_get(self):
        ht = HashTable()
        ht.set('jon', 'jons value')
        self.assertEqual(ht.get('jon'), 'jons value')
        ht.set('amy', 'amys value')
        self.assertEqual(ht.get('amy'), 'amys value')
        ht.set('lon', 'lons value')
        self.assertEqual(ht.get('lon'), 'lons value')
        # get a key that doesn't exist should raise a KeyError
        self.assertRaises(KeyError, ht.get, 'ron')



if __name__ == "__main__":
    unittest.main()
