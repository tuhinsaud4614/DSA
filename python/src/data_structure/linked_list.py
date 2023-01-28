"""Here we will create a Linked list"""

import json
from typing import Generic, List, Literal, Optional, TypeVar

from ..model.node import Node

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

    def push(self, data: T) -> None:
        """
        Add a node at the end of the `Linked List`
        :param data: T
        :type data: T
        """

        new_node = Node(data)
        if not self._head:
            self._head = new_node
            self._size += 1
            return

        current = self._head
        while current.right:
            current = current.right
        current.right = new_node
        self._size += 1

    def un_shift(self, data: T) -> int:
        """
        Add a node at the start of the `Linked List`
        :param data: T
        :type data: T
        :return: The size of the `Linked List`
        """

        new_node = Node(data)
        if not self._head:
            self._head = new_node
            self._size += 1
            return self._size

        new_node.right = self._head
        self._head = new_node
        self._size += 1
        return self._size

    def pop(self) -> Optional[T]:
        """
        Remove the last node of the `Linked List`.
        :return: The last value in the list
        """
        if not self._head:
            return None

        current = self._head
        while current.right:
            if not current.right.right:
                value = current.right.value
                current.right = None
                self._size -= 1
                return value

            current = current.right

        self._head = None
        self._size -= 1
        return current.value

    def shift(self) -> Optional[T]:
        """
        Remove the first node of the `Linked List`.
        :return: The first value in the list
        """
        if not self._head:
            return None

        value = self._head.value
        self._head = self._head.right
        self._size -= 1

        return value

    def insert_at(self, data: T, position: int) -> None:
        """
        It inserts data at a given index.

        :param data: The data to insert into the list
        :type data: T
        :param position: the position of the data to insert
        :type position: int
        :return: None
        """

        if not self._size >= position >= 0:
            return

        new_node = Node(data)

        if not self._head or position == 0:
            if position == 0:
                new_node.right = self._head
            self._head = new_node
            self._size += 1
            return

        current = self._head
        count = 0
        while count < position - 1 and current.right:
            count += 1
            current = current.right

        new_node.right = current.right
        current.right = new_node
        self._size += 1

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

        print("List: ", " -> ".join(map(str, items)))
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
