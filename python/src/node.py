"""
This is for the node.
"""

from typing import Any, Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """Defines a Node"""

    def __init__(self, value: T) -> None:
        """
        Creates an instance of `Node`

        This function takes in a value and returns None

        :param value: The value of the node
        :type value: any
        """
        self.left: Optional[Node[T]] = None
        self._value: T = value
        self.right: Optional[Node[T]] = None

    def to_object(self) -> dict[str, Any]:
        """
        It returns an object that represents the current node and its neighbors.
        :return: A dictionary with the id of the node, the value of the node, the next node, and the
        previous node.
        """
        return {
            "id": id(self),
            "value": self._value,
            "previous": self.left.to_object() if self.left else None,
            "next": self.right.to_object() if self.right else None
        }

    @property
    def value(self) -> T:
        """
        The is the `getter` for the value.
        :return: The value of the instance variable _value.
        """
        return self._value

    @value.setter
    def value(self, new_value: T) -> None:
        """
        The is the `setter` for the value.
        :param new_value: T
        :type new_value: T
        """
        self._value = new_value

    def __repr__(self) -> str:
        """
        Official representation of class

        The __repr__ function returns a string representation of the object
        :return: The class name.
        """
        return "<class 'Node'>"

    def __str__(self) -> str:
        """
        The magic method provides string representation of instance

        The `__str__` function is a special function that is called when you try to print an object
        :return: The name, attack power, and life of the character.
        """
        return f"Value: {self._value}"
