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



if __name__ == "__main__":
    unittest.main()
