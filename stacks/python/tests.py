import unittest

from stack import ListStack, NodeStack
from node import Node


class NodeTests:

    def test_init_node(self):
        """
        Tests initialization of Node
        """
        n1 = Node('data')
        self.assertIsInstance(n1, Node)
        self.assertEqual(n1.data, 'data')
        self.assertIsNone(n1.next)
        # make sure 'value' is writeable
        n1.data = "new_val"
        self.assertEqual(n1.data, 'new_val')
        # make sure 'next' is writeable
        n2 = Node('new_node')
        n1.next = n2


class TestStackList(unittest.TestCase):

    def setUp(self):
        self.stack = ListStack()

    def test_init_stack(self):
        """
        Test initialization of Stack
        """
        s = self.stack
        self.assertIsInstance(s, ListStack)
        self.assertEqual(s.size(), 0)
        self.assertTrue(s.is_empty())

    def test_push(self):
        """
        Tests the stack.push(data) method
        """
        s = self.stack
        self.assertEqual(s._items, [])
        self.assertEqual(s.size(), 0)

        # push
        s.push('a')
        self.assertEqual(s.size(), 1)
        self.assertEqual(s._items, ['a'])

        # push
        s.push('b')
        self.assertEqual(s.size(), 2)
        self.assertEqual(s._items, ['a', 'b'])

    def test_peek(self):
        """
        Tests the stack.peek() method
        """
        s = self.stack
        # peek on empty list should return None
        self.assertIsNone(s.peek())

        s.push('a')
        self.assertEqual(s.peek(), 'a')
        s.push('b')
        self.assertEqual(s.peek(), 'b')
        s.push('c')
        self.assertEqual(s.peek(), 'c')

    def test_pop(self):
        """
        Tests the stack.pop() method
        """
        s = self.stack
        # pop on empty list should return None
        self.assertIsNone(s.pop())

        # setup stack
        s.push('a')
        s.push('b')
        s.push('c')
        self.assertEqual(s.size(), 3)

        # start popping
        popped = s.pop()
        self.assertEqual(popped, 'c')
        self.assertEqual(s.size(), 2)

        popped = s.pop()
        self.assertEqual(popped, 'b')
        self.assertEqual(s.size(), 1)

        popped = s.pop()
        self.assertEqual(popped, 'a')
        self.assertEqual(s.size(), 0)

        popped = s.pop()
        self.assertEqual(popped, None)
        self.assertEqual(s.size(), 0)


class TestNodeStack(unittest.TestCase):

    def setUp(self):
        self.stack = NodeStack()

    def test_init_stack(self):
        """
        Test initialization of Stack
        """
        s = self.stack
        self.assertIsInstance(s, NodeStack)
        self.assertEqual(s._size, 0)
        self.assertEqual(s._first, None)
        self.assertEqual(s._last, None)

    def test_push(self):
        """
        Tests the stack.push(data) method
        """
        s = self.stack
        self.assertEqual(s.size(), 0)

        # push
        s.push('a')
        self.assertEqual(s._size, 1)
        self.assertEqual(s._first.get_data(), 'a')

        # push
        s.push('b')
        self.assertEqual(s._size, 2)
        self.assertEqual(s._first.get_data(), 'b')

    def test_peek(self):
        """
        Tests the stack.peek() method
        """
        s = self.stack
        # peek on empty list should return None
        self.assertIsNone(s.peek())

        s.push('a')
        self.assertEqual(s.peek(), 'a')
        s.push('b')
        self.assertEqual(s.peek(), 'b')
        s.push('c')
        self.assertEqual(s.peek(), 'c')

    def test_pop(self):
        """
        Tests the stack.pop() method
        """
        s = self.stack
        # pop on empty list should return None
        self.assertIsNone(s.pop())

        # setup stack
        s.push('a')
        s.push('b')
        s.push('c')
        self.assertEqual(s.size(), 3)

        # start popping
        popped = s.pop()
        self.assertEqual(popped, 'c')
        self.assertEqual(s.size(), 2)

        popped = s.pop()
        self.assertEqual(popped, 'b')
        self.assertEqual(s.size(), 1)

        popped = s.pop()
        self.assertEqual(popped, 'a')
        self.assertEqual(s.size(), 0)

        popped = s.pop()
        self.assertEqual(popped, None)
        self.assertEqual(s.size(), 0)


if __name__ == "__main__":
    unittest.main()
