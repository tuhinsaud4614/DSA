"""Main file"""
from src.data_structure.linked_list import LinkedList

if __name__ == "__main__":
    linked = LinkedList[int]()
    linked.push(10)
    linked.push(20)
    linked.push(30)
    linked.un_shift(0)
    linked.un_shift(50)
    linked.print_all()
    print("Size", linked.size)
    # print("Pop", linked.pop())
    # linked.print_all()
    # print("Size", linked.size)
    # print("Shift", linked.shift())
    # linked.print_all()
    # print("Size", linked.size)
    # print("Shift", linked.shift())
    # linked.print_all()
    # print("Size", linked.size)
    linked.insert_at(100, 4)
    linked.print_all()
    print("Size", linked.size)
