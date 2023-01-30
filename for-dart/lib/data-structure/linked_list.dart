import 'dart:convert';

import 'package:for_dart/model/node.dart';

enum PrintType { arrow, nested }

class LinkedList<T> {
  Node<T>? head;
  int size = 0;

  /// Add the data at the end of the `Linked List`.
  ///
  /// Args:
  ///   data (T): The new data to be added to the list.
  ///
  /// Returns:
  ///   The size of the list.
  int push(T data) {
    final newNode = Node(value: data);

    if (head == null) {
      head = newNode;
      return ++size;
    }

    var current = head;

    while (current!.next != null) {
      current = current.next;
    }
    current.next = newNode;

    return ++size;
  }

  /// Add the data at the start of the `Linked List`.
  ///
  /// Args:
  ///   data (T): The data that we want to add to the beginning of the list.
  ///
  /// Returns:
  ///   The size of the list
  int unShift(T data) {
    final newNode = Node(value: data);

    if (head == null) {
      head = newNode;
      return ++size;
    }

    newNode.next = head;
    head = newNode;
    return ++size;
  }

  /// Remove the last node of the `Linked List`.
  ///
  /// Returns:
  ///   The last value in the linked list.
  T? pop() {
    if (head == null) {
      return null;
    }

    var current = head;
    while (current != null && current.next != null) {
      if (current.next!.next == null) {
        final value = current.next!.value;
        current.next = null;
        --size;
        return value;
      }
      current = current.next;
    }
    head = null;
    --size;
    return current!.value;
  }

  /// Remove the first node of the `Linked List`.
  ///
  /// Returns:
  ///   The first value in the list
  T? shift() {
    if (head == null) {
      return null;
    }

    final value = head!.value;
    head = head!.next;
    --size;
    return value;
  }

  /// It inserts data at a given position.
  ///
  /// Args:
  ///   data (T): The data to be inserted.
  ///   position (int): The position where the new node should be inserted.
  ///
  void insertAt(T data, int position) {
    if (position > size || position < 0) {
      return;
    }

    final newNode = Node(value: data);

    if (head == null || position == 0) {
      if (position == 0) {
        newNode.next = head;
      }

      head = newNode;
      ++size;
      return;
    }

    var current = head;
    var count = 0;

    while (count < position - 1 && current?.next != null) {
      count += 1;
      current = current!.next;
    }

    newNode.next = current?.next;
    current?.next = newNode;
    ++size;
  }

  /// Print all the items of the `LinkedList`.
  ///
  /// Args:
  ///   type (PrintType): This is an enum that allows you to print the linked list in two different
  /// ways. Defaults to PrintType
  ///
  /// Returns:
  ///   A list of all the values in the linked list.
  void printAll([PrintType type = PrintType.arrow]) {
    if (head == null) {
      print("The linked list is empty");
      return;
    }

    if (type == PrintType.nested) {
      var encoder = JsonEncoder.withIndent("  ");
      print("List: ${encoder.convert(head?.toObject())}");
      return;
    }

    List<T> list = [];
    Node<T>? current = head;

    if (current != null) {
      list.add(current.value);

      while (current!.next != null) {
        current = current.next;
        if (current != null) {
          list.add(current.value);
        }
      }
    }
    print('List: ${list.join(" -> ")}');
  }
}
