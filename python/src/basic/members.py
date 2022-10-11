"""
Class can have class variables as well as instance variables.

Class variables are shared across all instances while instance
variables are only limited to that particular instance
"""


class Character:
    """Defines a character"""

    def __init__(self, name: str, attack_power: int, life: int) -> None:
        """
        Creates an instance of `Character`

        This function takes in a name, attack power, and life and returns None

        :param name: The name of the character
        :type name: str
        :param attack_power: The amount of damage this character can do to another character
        :type attack_power: int
        :param life: The amount of life the character has
        :type life: int
        """
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __repr__(self) -> str:
        """
        Official representation of class

        The __repr__ function returns a string representation of the object
        :return: The class name.
        """
        return "<class 'Character'>"

    def __str__(self) -> str:
        """
        The magic method provides string representation of instance

        The `__str__` function is a special function that is called when you try to print an object
        :return: The name, attack power, and life of the character.
        """
        return f"Name: {self.name}, Attack Power: {self.attack_power}, Life: {self.life}"


class Person:
    """Defines a person"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """
        Creates an instance of `Person`

        The function __init__ takes two strings as arguments, first_name and last_name, and assigns them
        to the instance variables first_name and last_name

        :param first_name: str
        :type first_name: str
        :param last_name: str
        :type last_name: str
        """
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        """
        Official representation of class

        The __repr__ function returns a string representation of the object
        :return: The class name.
        """
        return "<class 'Person'>"

    def __str__(self) -> str:
        """
        The magic method provides string representation of instance
        The __str__() function returns a string representation of the object
        :return: The first and last name of the person.
        """
        return f"Fullname: {self.first_name} {self.last_name}"


class Box:
    """Defines a box"""

    # Class Variables/Members
    box_type: str = "Packing Carton"
    color: str = "Brown"

    def __init__(self, side_a: int, side_b: int) -> None:
        """
        Creates an instance of `Box`

        This function takes two integers as arguments and assigns them to the instance variables first_name and last_name

        :param side_a: int
        :type side_a: int
        :param side_b: int
        :type side_b: int
        """
        # Instance Variables/Members
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self) -> str:
        """
        Official representation of class

        The __repr__ function returns a string representation of the object
        :return: The class name.
        """
        return "<class 'Box'>"

    def __str__(self) -> str:
        """
        The magic method provides string representation of instance
        The __str__() function returns a string representation of the object
        :return: The string representation of the object.
        """
        return f"Side A: {self.side_a}, Side B: {self.side_b}"


Box.color = "Green"

box1 = Box(10, 20)
box1.color = "Red"  # Set color to instance variable as Red
print(box1)  # Side A: 10, Side B: 20
print(box1.color)  # Red
print(hex(id(box1)))  # Location id of box1 instance
print(Box.color)  # Green
