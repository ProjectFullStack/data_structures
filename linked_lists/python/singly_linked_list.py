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

