import unittest
from node import Node


class TestNodeClass(unittest.TestCase):

    def test_node_init(self):
        """
        Test new Node initialization
        """
        node1 = Node(17)
        self.assertEqual(node1.get_data(), 17)
        self.assertIsNone(node1.get_next(), None)

    def test_node_setters(self):
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



if __name__ == "__main__":
    unittest.main()
