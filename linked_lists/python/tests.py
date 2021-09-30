import unittest
from node import Node
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def test_list_init(self):
        """
        Test new SinglyLinkedList initialization
        """
        ll = SinglyLinkedList()
        self.assertIsInstance(ll, SinglyLinkedList)
        self.assertEqual(ll.size(), 0)
        self.assertIsNone(ll.head)

    def test_add(self):
        """
        Tests the SinglyLinkedList.add(data) method
        """
        ll = SinglyLinkedList()

        # push first Node
        insert_data = 15
        ll.add(insert_data)
        self.assertIsInstance(ll.head, Node)
        self.assertEqual(ll.head.get_data(), insert_data)
        self.assertEqual(ll.size(), 1)

        # push second Node
        insert_data = 23
        ll.add(insert_data)
        self.assertIsInstance(ll.head, Node)
        self.assertEqual(ll.head.get_data(), insert_data)
        self.assertEqual(ll.size(), 2)

    def test_search(self):
        """
        Tests the SinglyLinkedList.search(item) method
        """
        ll = SinglyLinkedList()

        # check if searching on empty list returns false
        item = 123
        self.assertFalse(ll.search(item))

        # add some nodes
        ll.add(23)
        ll.add(17)
        ll.add(382)

        # check if searching for a value in list returns true
        self.assertTrue(ll.search(17))

        # check if searching for a value not in list returns false
        self.assertFalse(ll.search(123123123))

        # check if searching for a different data type (strings) that what
        # our nodes holds throws any errors
        self.assertFalse(ll.search("hello world!"))

    def test_remove(self):
        """
        Tests the SinglyLinkedList.remove(item) method
        """
        # test remove on an empty list, should throw a ValueError
        ll = SinglyLinkedList()
        self.assertRaises(ValueError, ll.remove, 17)

        # add some nodes
        ll.add(23)
        ll.add(17)
        ll.add(382)

        # list should be 382 -> 17 -> 23
        # first try remove the middle one
        self.assertTrue(ll.search(17))
        ll.remove(17)
        self.assertFalse(ll.search(17))

        # list should now be 382 -> 23
        # lets try removing the head (382)
        self.assertTrue(ll.search(382))
        ll.remove(382)
        self.assertFalse(ll.search(382))
        # also searching for the tail (23) to make sure we didn't break it
        self.assertTrue(ll.search(23))
        # and verify the head is now 23
        self.assertEqual(ll.head.get_data(), 23)

    def test_append(self):
        """
        Tests the SinglyLinkedList.append(item) method
        """
        # test on empty list, the head should then point to the appended item
        ll = SinglyLinkedList()
        ll.append(10)
        self.assertTrue(ll.head.get_data(), 10)




if __name__ == "__main__":
    unittest.main()
