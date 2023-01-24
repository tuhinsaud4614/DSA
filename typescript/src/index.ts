import { LinkedList } from "data-structure";
import { MyNode } from "model";

const linkedList = new LinkedList();
linkedList.push(new MyNode(10));
linkedList.push(new MyNode(20));
// linkedList.push(new MyNode(30));
// linkedList.unshift(new MyNode(0));
// linkedList.unshift(new MyNode(50));
linkedList.printAll();
// console.log("Pop:", linkedList.pop());
// linkedList.printAll();
console.log("Shift:", linkedList.shift());
linkedList.printAll();
