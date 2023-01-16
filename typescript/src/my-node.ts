/** Defines a Node */

import {  NotFunction } from "./types";

class MyNode<T> {
  /** This is for it's `left` node. This is a private property. */
  #left: MyNode<T> | null;
  /* This is for it's `right` node. This is a private property. */
  #right: MyNode<T> | null;
  /* This is for it's `right` node. This is a private property. */
  #value: NotFunction<T>;

  /**
   * Creates an instance of `Node`.
   * The above function is a constructor function. It takes a value of type `NotFunction<T>` and
   * assigns it to the private property `#value`
   * @param value - NotFunction<T>
   */
  constructor(value: NotFunction<T>) {
    this.#value = value;
  }

  /**
   * The is the `getter` for the value.
   * @returns The value of the private property `#value`.
   */
  get value() {
    return this.#value;
  }

  /**
   * It sets the value of the private variable `#value` to the value passed in.
   * @param value - The value to be checked.
   */
  set value(value: NotFunction<T>) {
    this.#value = value;
  }

  /**
   * The is the `getter` for the __Node__ `left`.
   * @returns The value of the private property `#left`.
   */
  get left(): MyNode<T> | null {
    return this.#left;
  }

  /**
   * It sets the value of the private variable `#left` to the value passed in.
   * @param value - The value to be checked.
   */
  set left(node: MyNode<T> | null) {
    this.#left = node;
  }

  /**
   * The is the `getter` for the __Node__ `right`.
   * @returns The value of the private property `#right`.
   */
  get right(): MyNode<T> | null {
    return this.#right;
  }

  /**
   * It sets the value of the private variable `#right` to the value passed in.
   * @param value - The value to be checked.
   */
  set right(node: MyNode<T> | null) {
    this.#right = node;
  }
}

export default MyNode;
