import 'dart:convert';

import 'package:for_dart/model/node.dart';

enum PrintType { arrow, nested }

class LinkedList<T> {
  Node<T>? head;
  int size = 0;

  /// Add a node at the end of the `Linked List`.
  ///
  /// Args:
  ///   newNode (Node<T>): The new node to be added to the list.
  ///
  /// Returns:
  ///   The size of the list.
  int push(Node<T> newNode) {
    if (head == null) {
      head = newNode;
      return ++size;
    }

    Node<T>? current = head;

    while (current?.next != null) {
      current = current?.next;
    }
    current?.next = newNode;

    return ++size;
  }

  /// Add a node at the start of the `Linked List`.
  ///
  /// Args:
  ///   newNode (Node<T>): The node that we want to add to the beginning of the list.
  ///
  /// Returns:
  ///   The size of the list
  int unShift(Node<T> newNode) {
    if (head == null) {
      head = newNode;
      return ++size;
    }

    newNode.next = head;
    head = newNode;
    return ++size;
  }

  /// Print all the items of the `LinkedList`.
  ///
  /// Args:
  ///   type (PrintType): This is an enum that allows you to print the linked list in two different
  /// ways. Defaults to PrintType
  ///
  /// Returns:
  ///   A list of all the values in the linked list.
  printAll([PrintType type = PrintType.arrow]) {
    if (head == null) {
      print("The linked list is empty");
      return;
    }

    if (type == PrintType.nested) {
      var encoder = JsonEncoder.withIndent("  ");
      print(encoder.convert(head?.toObject()));
      return;
    }

    List<T> list = [];
    Node<T>? current = head;

    if (current != null) {
      list.add(current.value);

      while (current?.next != null) {
        current = current?.next;
        if (current != null) {
          list.add(current.value);
        }
      }
    }
    print(list.join(" -> "));
  }
}
