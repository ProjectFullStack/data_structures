"""
singly_linked_list.py
Implements a singly linked listed (unsorted)
projectfullstack
20210930
"""

from node import Node


class SinglyLinkedList:
    """
    Unsorted Singly Linked List implementation

    Methods:
        - is_empty - O(1) - checks if the list is empty
        - add(item) - O(1) - adds new item to head of list
        - length() - O(n) - returns the length of the list
        - search(item) - O(n) - checks if item in list, True if found,
                                else false
        - remove(item) - O(n) - checks if item in list, removes it if found,
                                throws ValueError if not found
        - append(item) - O(n) - appends item to end of list
    """

    def __init__(self):
        """
        Singly List List constructor
        """
        self._head = None
        self._length = 0

    def __str__(self):
        """
        String representation
        :return: example: "[0,12,3,2]"
        :rtype: str
        """
        result = "["
        current_node = self.head
        while current_node is not None:
            result += str(current_node.get_data())
            if current_node.get_next() is not None:
                result += ", "
            current_node = current_node.get_next()
        result += "]"
        return result

    @property
    def head(self):
        """
        Returns the head of the list
        :return: The head of the list
        :rtype: Node or None
        """
        return self._head

    @head.setter
    def head(self, node):
        """
        Sets the head of the list
        :param node: the Node which should be the new head
        :type node: Node
        """
        self._head = node

    def is_empty(self):
        """
        checks if the list is empty
        :return: True if list is empty, else False
        :rtype: bool
        """
        return self._head is None

    def add(self, item):
        """
        Adds new a node node with the given data to the beginning of the list
        :param item: the data the node will hold
        :type item: any
        """
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """
        Returns the length of the list
        :return: the length of the list
        :rtype: int
        """
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, item):
        """
        Searches the list for the given item,
        :param item: The item or data to search for
        :type item: any
        :return: if key is found returns True, else False
        :rtype: bool
        """
        current_node = self.head
        found = False
        while current_node is not None and not found:
            if current_node.get_data() == item:
                found = True
            else:
                current_node = current_node.get_next()
        return found

    def remove(self, item):
        """
        Removes the given item if found in list
        :param item: the item or data to search for
        :type item: any
        """
        current_node = self.head
        previous = None

        while current_node is not None:
            if current_node.get_data() == item:
                break  # stop the while loop
            previous = current_node
            current_node = current_node.get_next()

        if current_node is None:
            # iterated through entire list without finding the item
            # throw error
            raise ValueError(f"{item} is not in the list")

        if previous is None:
            # the node to remove is the at the head
            self.head = current_node.get_next()
        else:
            # the node to remove is not at the head
            previous.set_next(current_node.get_next())

    def append(self, item):
        """
        Appends item to the end of the list
        :param item:
        :type item:
        :return:
        :rtype:
        """
        new_node = Node(item)
        if self.head is None:
            self. head = new_node
        else:
            current_node = self.head
            while current_node.get_next() is not None:
                current_node = current_node.get_next()
            current_node.set_next(new_node)
