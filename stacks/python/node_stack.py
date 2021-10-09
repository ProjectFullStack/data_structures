"""
Stack
ProjectFullStack
20211008

NodeStack - Stack implementation use nodes and a linked list style data struct
"""

from node import Node


class NodeStack:
    """
    LiFo (Last In First Out) Stack implementation that uses
    nodes and linked list style of data structure

    Methods:
        size - O(1) - Returns the number of items in the stack
        is_empty - O(1) -checks if stack is empty
        push(data) - O(1) - add new data onto top of stack
        pop() - O(1) - Pops from top of stack
        peek() - O(1) - Returns the data on the top of the stack
    """

    def __init__(self):
        """
        Constructor
        """
        self._first = None
        self._last = None
        self._size = 0

    def size(self):
        """
        Returns the number of items in the stack
        :return: the number of items in the stack
        :rtype: int
        """
        return self._size

    def is_empty(self):
        """
        Checks if the stack is empty O(1)
        :return: true if empty, else false
        :rtype: bool
        """
        return self._size == 0

    def push(self, item):
        """
        Adds a new item to the top of the stack
        :param item: the data to add
        :type item: any
        """
        new_node = Node(item)
        if self._size == 0:
            self._first = new_node
            self._last = new_node
        else:
            temp_node = self._first
            new_node.set_next(temp_node)
            self._first = new_node
        self._size += 1

    def pop(self):
        """
        Removes the top item from the stack
        :return: the top item
        :rtype: any
        """
        if self._size == 0:
            return None
        if self._size == 1:
            self._last = None
        popped_node = self._first
        self._first = self._first.get_next()
        popped_node.set_next(None)
        self._size -= 1
        return popped_node.get_data()

    def peek(self):
        """
        Gets the value of the top item from the stack, does not modify the
        stack
        :return: The top item
        :rtype: any
        """
        if self._size == 0:
            return None
        return self._first.get_data()
