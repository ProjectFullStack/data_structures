"""
SinglyLinkedList
ProjectFullStack
20211002
"""

from node import Node


class SinglyLinkedList:
    """
    SinglyLinkedList Class
    Methods:
        add(item) - O(1) - add item to beginning of the list
        search(item) - O(1) - search for the item in the list, return boolean
        index(item) - O(1) - search for the item in the list, return the index
        remove(item) - O(n) to find it, O(1) to remove
                - removes the FIRST item in the list
    """

    def __init__(self):
        """
        Constructor for the SinglyLinkedList class
        """
        self._head = None

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
        Getter for the head property
        :return: the head of the list
        :rtype: Node or None
        """
        return self._head

    @head.setter
    def head(self, node):
        """
        Setter for the head property
        :param node: The node that will become the new head
        :type node: Node
        """
        self._head = node

    def add(self, data):
        """
        Adds a new data item to the head of the list
        :param data: the data to add
        :type data: Any
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, item):
        """
        Searches for item in the list, returns true if it is found, else false
        :param item: the item to search for
        :type item: any
        :return: true if not found, else false
        :rtype: bool
        """
        current_node = self.head
        while current_node is not None and current_node.get_data() != item:
            current_node = current_node.get_next()
        return current_node is not None

    def index(self, item):
        """
        Searches for item in the list, returns the index it is found at,
        else -1
        :param item: the item to search for
        :type item: any
        :return: -1 if not found, else the index it is found at
        :rtype: int
        """
        # fail fast
        if self.head is None:
            return -1

        current_node = self.head
        index = 0
        while current_node.get_data() != item:
            current_node = current_node.get_next()
            index += 1
            if current_node is None:
                return -1

        return index

    def remove(self, item):
        """
        Removes the first instance of item from the list
        :param item: The item to search for to remove
        :type item: any
        """
        current_node = self.head
        prev_node = None
        found = False

        while not found and current_node is not None:
            if current_node.get_data() == item:
                found = True
            else:
                prev_node = current_node
                current_node = current_node.get_next()

        if current_node is None:
            raise ValueError(f"the item: {item}, is not in the list")

        # if we get down here, the current_node is the node we want to remove
        if prev_node is None:
            # this happens if we are removing the head of the list
            self.head = current_node.get_next()
            current_node.set_next(None)
        else:
            prev_node.set_next(current_node.get_next())
            current_node.set_next(None)

    def is_empty(self):
        """
        Returns true if list is empty, else false
        :return: true if list is empty, else false
        :rtype: bool
        """
        return self.head is None

    def size(self):
        """
        Returns the size of the linked list
        :return: the number of nodes in the linked list
        :rtype: int
        """
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count
