import { MyNode } from "model";

export default class LinkedList<T> {
  #head?: MyNode<T> = undefined;
  #size = 0;

  /**
   * Add a node at the end of the `Linked List`.
   * @param newNode - MyNode<T> - This is the node that we want to add to the end of the list.
   * @returns The size of the list
   */
  push(newNode: MyNode<T>) {
    if (!this.#head) {
      this.#head = newNode;
      return ++this.#size;
    }

    let current = this.#head;

    while (current.right) {
      current = current.right;
    }

    current.right = newNode;
    return ++this.#size;
  }

  /**
   * Add a node at the start of the `Linked List`.
   * @param newNode - MyNode<T>
   * @returns The size of the list
   */
  unshift(newNode: MyNode<T>) {
    if (!this.#head) {
      this.#head = newNode;
      return ++this.#size;
    }

    newNode.right = this.#head;
    this.#head = newNode;
    return ++this.#size;
  }

  /**
   * Remove the last node of the `Linked List`.
   * @returns The last value in the list.
   */
  pop(): T | undefined {
    if (!this.#head) {
      return undefined;
    }

    let current = this.#head;

    while (current.right) {
      if (!current.right.right) {
        const value = current.right.value;
        current.right = null;
        return value;
      }

      current = current.right;
    }

    return undefined;
  }

  /**
   * Remove the first node of the `Linked List`.
   * @returns The first value in the list
   */
  shift(): T | undefined {
    if (!this.#head) {
      return undefined;
    }

    const value = this.#head.value;
    this.#head = this.#head.right || undefined;
    return value;
  }

  /**
   * Print all the items of the `LinkedList`.
   * @param {"nested" | "arrow"} [type=arrow] - "nested" | "arrow" = "arrow"
   * @returns The values of the linked list.
   */
  printAll(type: "nested" | "arrow" = "arrow") {
    if (!this.#head) {
      console.log("The linked list is empty");
      return;
    }

    if (type === "nested") {
      console.log(JSON.stringify(this.#head.toObject(), null, 2));
      return;
    }

    const list: T[] = [];
    let current = this.#head;
    list.push(current.value);

    while (current.right) {
      current = current.right;
      list.push(current.value);
    }
    console.log("List: ", list.join(" -> "));
  }

  /**
   * The size property is a getter that returns the value of the private `#size` property
   * @returns The size of the `LinkedList`.
   */
  get size() {
    return this.#size;
  }
}
