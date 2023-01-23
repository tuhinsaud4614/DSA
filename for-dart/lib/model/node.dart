class Node<T> {
  Node<T>? previous;
  Node<T>? next;
  final T value;

  Node({required this.value});

  /// If this node has a value, then return a map with the value, and the previous and next nodes, if
  /// they exist.
  ///
  /// Returns:
  ///   A map of the object's properties.
  Map<String, dynamic> toObject() {
    return ({
      "id": identityHashCode(this),
      "value": value,
      "previous": previous?.toObject(),
      "next": next?.toObject()
    });
  }
}
