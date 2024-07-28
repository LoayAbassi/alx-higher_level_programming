#!/usr/bin/python3
"""
100-singly_linked_list.oy
Description:
This module contains the definition of a singly linked list.
a class node that defines a single node's elements and a singlyLinkedList 
class that defines the linked list itself and do the adding of elements.

"""
class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node or None): The reference to the next node in the list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new node with given data and next_node reference.

        Args:
            data (int): The data to store in the node.
            next_node (Node or None): The next node in the list (default is None).
        """
        self.__next_node = next_node
        self.__data = data

    @property
    def data(self):
        """
        Gets the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, data):
        """
        Sets the data of the node.

        Args:
            data (int): The data to store in the node.

        Raises:
            TypeError: If the provided data is not an integer.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """
        Gets the reference to the next node.

        Returns:
            Node or None: The next node in the list or None if there is no next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """
        Sets the reference to the next node.

        Args:
            next_node (Node or None): The next node in the list.

        Raises:
            TypeError: If next_node is neither a Node object nor None.
        """
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        __head (Node or None): The head node of the linked list.
    """
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string with each node's data on a new line.
        """
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The data to be inserted into the list.

        The new node is inserted such that the list remains sorted in ascending order.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
