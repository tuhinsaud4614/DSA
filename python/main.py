"""Main file"""
from src.data_structure.linked_list import LinkedList
from src.model.node import Node

if __name__ == "__main__":
    linked = LinkedList[int]()
    linked.push(Node(10))
    linked.push(Node(20))
    linked.push(Node(30))
    linked.un_shift(Node(0))
    linked.un_shift(Node(50))
    linked.print_all()
    print("Pop", linked.pop())
    linked.print_all()
    print("Shift", linked.shift())
    print("Shift", linked.shift())
    linked.print_all()
