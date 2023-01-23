"""Here we will create a Linked list"""

import json
from typing import Generic, List, Literal, Optional, TypeVar

from ..node import Node

T = TypeVar("T")


class LinkedList(Generic[T]):
    """Defines a Linked List"""

    def __init__(self) -> None:
        """
        Creates an instance of `Linked List`
        :type value: None
        """
        self._head: Optional[Node[T]] = None
        self._size = 0

    def push(self, new_node: Node[T]) -> None:
        """
        Add a node at the end of the `Linked List`
        :param new_node: Node[T]
        :type new_node: Node[T]
        """

        if not self._head:
            self._head = new_node
            self._size += 1
            return

        current = self._head
        while current.right:
            current = current.right
        current.right = new_node
        self._size += 1

    def un_shift(self, new_node: Node[T]) -> int:
        """
        Add a node at the start of the `Linked List`
        :param new_node: Node[T]
        :type new_node: Node[T]
        :return: The size of the `Linked List`
        """

        if not self._head:
            self._head = new_node
            self._size += 1
            return self._size

        new_node.right = self._head
        self._head = new_node
        self._size += 1
        return self._size

    def print_all(self, type_as: Literal["nested", "arrow"] = "arrow") -> None:
        """
        This will print all the items in the `Linked List`.
        """
        if not self._head:
            print("No item found!")
            return

        if type_as == "nested":
            print(json.dumps(self._head.to_object(), indent=2))
            return

        current = self._head
        items: List[T] = []
        items.append(current.value)

        while current.right:
            current = current.right
            items.append(current.value)

        print(" -> ".join(map(str, items)))
        return

    @property
    def size(self) -> int:
        """
        The is the `getter` for the `size`.
        :return: The value of the instance variable `_size`.
        """
        return self._size

    def __repr__(self) -> str:
        """
        Official representation of class

        The __repr__ function returns a string representation of the object
        :return: The class name.
        """
        return "<class 'LinkedList'>"

    def __str__(self) -> str:
        """
        The magic method provides string representation of instance

        The `__str__` function is a special function that is called when you try to print an object
        """
        return f"Value: {self}"
