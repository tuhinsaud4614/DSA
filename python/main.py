"""Main file"""
from src.data_structure.linked_list import LinkedList
from src.node import Node

if __name__ == "__main__":
    linked = LinkedList[int]()
    linked.push(Node(10))
    linked.push(Node(30))
    linked.push(Node(20))
    linked.un_shift(Node(0))
    linked.un_shift(Node(50))
    #pylint: disable=E1121
    linked.print_all()
