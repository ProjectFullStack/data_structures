"""
Stack
ProjectFullStack
20211008

ListStack - Stack implementation using python built in list
"""


class ListStack:
    """
    LiFo (Last In First Out) Stack implementation that uses
    python built in list to store stack items

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
        self._items = []

    def size(self):
        """
        Returns the number of items in the stack
        :return: the number of items in the stack
        :rtype: int
        """
        return len(self._items)

    def is_empty(self):
        """
        Checks if the stack is empty O(1)
        :return: true if empty, else false
        :rtype: bool
        """
        return self.size() == 0

    def push(self, item):
        """
        Adds a new item to the top of the stack
        :param item: the data to add
        :type item: any
        """
        self._items.append(item)

    def pop(self):
        """
        Removes the top item from the stack
        :return: the top item
        :rtype: any
        """
        if self.size() == 0:
            return None
        return self._items.pop()

    def peek(self):
        """
        Gets the value of the top item from the stack, does not modify the
        stack
        :return: The top item
        :rtype: any
        """
        if self.size() == 0:
            return None
        return self._items[-1]
