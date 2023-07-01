#!/usr/bin/python3
"""linked list"""


class Node:
    """Node"""

    def __init__(self, data, next_node=None):
        """init
        Args:
            data: int number
            next_node: next node pointer
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter and validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter and validation"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self):
        """init
        Args:
            __head: head pointer
        """
        self.__head = None

    def sorted_insert(self, value):
        """insert in sorted list
        Args:
            value: the value of the new node
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            if value < self.__head.data:
                self.__head = Node(value, self.__head)
            else:
                next_node = self.__head.next_node
                perv_node = self.__head
                while next_node is not None:
                    if value < next_node.data:
                        perv_node.next_node = Node(value, next_node)
                        break
                    next_node = next_node.next_node
                    perv_node = perv_node.next_node
                else:
                    perv_node.next_node = Node(value)

    def __str__(self):
        """get object string"""
        t = ""
        current = self.__head
        while current:
            t += (str(current.data) + ("\n" if current.next_node
                                       else ""))
            current = current.next_node
        return t
