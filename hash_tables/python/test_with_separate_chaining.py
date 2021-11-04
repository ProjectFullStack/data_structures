import unittest
from hash_table_with_separate_chaining import HashTable


class TestWithSeparateChaining(unittest.TestCase):

    def test_init(self):
        """
        Test new Node initialization
        """
        ht = HashTable()
        self.assertIsInstance(ht, HashTable)
        self.assertEqual(ht.size, 9)
        self.assertEqual(ht._map, [None] * 9)

    def test_hash(self):
        ht = HashTable()
        self.assertEqual(ht._hash('jon'), 3)
        self.assertEqual(ht._hash('amy'), 3)
        self.assertEqual(ht._hash('mike'), 4)
        self.assertEqual(ht._hash('123456789'), 0)

    def test_set(self):
        ht = HashTable()
        ht.set('jon', 'jons value')
        self.assertEqual(ht._map[3], [['jon', 'jons value']])
        ht.set('mike', 'mikes value')
        self.assertEqual(ht._map[4], [['mike', 'mikes value']])
        # amy will overwrite jon
        ht.set('amy', 'amys value')
        self.assertEqual(ht._map[3], [['jon', 'jons value'], ['amy', 'amys value']])

    def test_get(self):
        ht = HashTable()
        ht.set('jon', 'jons value')
        self.assertEqual(ht.get('jon'), 'jons value')
        ht.set('mike', 'mikes value')
        self.assertEqual(ht.get('mike'), 'mikes value')
        # amy will overwrite jon
        ht.set('amy', 'amys value')
        self.assertEqual(ht.get('amy'), 'amys value')
        # jon will still return jons value, amy will NOT have over written jon
        self.assertEqual(ht.get('jon'), 'jons value')

    def test_keys(self):
        ht = HashTable()
        ht.set('jon', 'jons value')
        ht.set('mike', 'mikes value')
        self.assertEqual(ht.keys(), ['jon', 'mike'])
        ht.set('amy', 'amys value')
        self.assertEqual(ht.keys(), ['jon', 'amy', 'mike'])



if __name__ == "__main__":
    unittest.main()
