import unittest
from node import Node
from singly_linked_list import SinglyLinkedList


class TestNodeClass(unittest.TestCase):

    def test_node_init(self):
        """
        Test new Node initialization
        """
        node1 = Node(17)
        self.assertEqual(node1.get_data(), 17)
        self.assertIsNone(node1.get_next(), None)

    def test_node_setters(self):
        """
        Tests the setter methods for the next and data instance variables
        """
        node1 = Node(17)

        # test setter for the data variable
        node2 = Node(23)
        self.assertEqual(node2.get_data(), 23)
        node2.set_data(99)
        self.assertEqual(node2.get_data(), 99)

        # test setter for the next variable
        self.assertIsNone(node1.get_next(), None)
        node1.set_next(node2)
        self.assertEqual(node1.get_next(), node2)
        self.assertIsNone(node2.get_next(), None)

    def test_ll_init(self):
        """
        Test new SinglyLinkedList initialization
        """
        ll = SinglyLinkedList()
        self.assertIsNone(ll.head, None)

    def test_ll_add(self):
        """
        Test new SinglyLinkedList add method, which adds a new node to the
        head of the list
        """
        ll = SinglyLinkedList()
        self.assertIsNone(ll.head, None)

        # add node 1 with data of 17
        ll.add(17)
        self.assertIsInstance(ll.head, Node)
        self.assertEqual(ll.head.get_data(), 17)

        # add node 2 with data of 31
        ll.add(31)
        self.assertIsInstance(ll.head, Node)
        self.assertEqual(ll.head.get_data(), 31)

        # ll should be [31, 17]. Make sure the first node 31 has a pointer
        # to the next node of 17
        self.assertEqual(ll.head.get_next().get_data(), 17)

    def test_ll_search(self):
        """
        Test new SinglyLinkedList search method, which checks if a given item
        is in the list
        """
        ll = SinglyLinkedList()
        self.assertIsNone(ll.head, None)

        # test searching across empty list does not give error
        self.assertFalse(ll.search(99))

        # add elements and test for elements that are in the list
        ll.add(17)
        self.assertTrue(ll.search(17))
        ll.add(23)
        self.assertTrue(ll.search(17))
        self.assertTrue(ll.search(23))
        ll.add(49)
        self.assertTrue(ll.search(17))
        self.assertTrue(ll.search(23))
        self.assertTrue(ll.search(49))

        # test for elements that are not in the list
        self.assertFalse(ll.search(99))
        self.assertFalse(ll.search(10))
        self.assertFalse(ll.search(-5))
        self.assertFalse(ll.search(43.7))

    def test_ll_index(self):
        """
        Test new SinglyLinkedList index method, which checks if a given item
        is in the list and returns the index where it is
        """
        ll = SinglyLinkedList()
        self.assertIsNone(ll.head, None)

        # test searching across empty list does not give error
        self.assertEqual(ll.index(99), -1)

        # add elements and test for elements that are in the list
        ll.add(17)
        self.assertEqual(ll.index(17), 0)
        ll.add(23)
        self.assertEqual(ll.index(17), 1)
        self.assertEqual(ll.index(23), 0)
        ll.add(49)
        self.assertEqual(ll.index(17), 2)
        self.assertEqual(ll.index(23), 1)
        self.assertEqual(ll.index(49), 0)

        # test for elements that are not in the list
        self.assertEqual(ll.index(99), -1)
        self.assertEqual(ll.index(10), -1)
        self.assertEqual(ll.index(-5), -1)
        self.assertEqual(ll.index(43.7), -1)

    def test_ll_remove(self):
        """
        Test new SinglyLinkedList remove method, which will remove the first
        node with a given value, it does NOT return the removed node
        """
        ll = SinglyLinkedList()
        self.assertIsNone(ll.head, None)

        # test remove on empty list, should raise Value error
        self.assertRaises(ValueError, ll.remove, 99)

        # add elements and test for elements that are in the list
        ll.add(17)
        ll.add(23)
        ll.add(49)

        # [49, 23, 17] remove the head node (49)
        self.assertTrue(ll.head.get_data(), 49)
        self.assertTrue(ll.search(49))
        ll.remove(49)
        self.assertFalse(ll.search(49))
        # and check that 23 begins the new head
        self.assertTrue(ll.head.get_data(), 23)

        # [23, 17] remove the tail node (17)
        self.assertTrue(ll.search(17))
        ll.remove(17)
        self.assertFalse(ll.search(17))

        ll.add(99)
        ll.add(87)
        # [87, 99, 23] remove a middle node (99)
        self.assertTrue(ll.head.get_data(), 87)
        self.assertTrue(ll.search(99))
        ll.remove(99)
        self.assertFalse(ll.search(99))
        # and check that the head has not changed
        self.assertTrue(ll.head.get_data(), 87)

        # [87, 23]
        # add some duplicates, test that the remove function
        # removes only the first item, not ALL the times
        ll.add(19)
        ll.add(19)
        ll.add(100)
        # [100, 19, 19, 87, 23]
        self.assertTrue(ll.head.get_data(), 100)
        self.assertTrue(ll.search(19))
        ll.remove(19)
        self.assertTrue(ll.search(19))  # true because should be one more 19
        ll.remove(19)
        self.assertFalse(ll.search(19)) # now false
        # and check that 100 is still the head
        self.assertTrue(ll.head.get_data(), 100)

        # test for removing items that don't exist
        self.assertRaises(ValueError, ll.remove, -100)





if __name__ == "__main__":
    unittest.main()
