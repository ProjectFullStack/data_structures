"""
node.py
projectfullstack
20210930
"""


class Node:
    """
    Class representation of a Node element. A node will hold data and a
    pointer to another node
    """

    def __init__(self, data):
        """
        Node constructor
        :param data: the data the node will holde
        :type data: any
        """
        self._data = data
        self._next = None

    def __str__(self):
        """
        Returns the string representation of a Node object
        :return: the string representation
        :rtype: string
        """
        return str(f"{self._data}")

    def get_data(self):
        """
        Gets the nodes data
        :return: the nodes data
        :rtype: any
        """
        return self._data

    def set_data(self, data):
        """
        Sets the nodes data
        :param data: the data to set
        :type data: any
        """
        self._data = data

    def get_next(self):
        """
        Returns the next node
        :return: the next node
        :rtype: Node | None
        """
        return self._next

    def set_next(self, node):
        """
        Sets the next node
        :param node: the next node
        :type node: Node
        """
        self._next = node
