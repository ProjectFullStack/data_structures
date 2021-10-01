from node import Node


class SinglyLinkedList:

    def __init__(self):
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
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

