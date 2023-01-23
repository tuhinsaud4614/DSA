import { LinkedList } from "data-structure";
import { MyNode } from "model";

const linkedList = new LinkedList();
linkedList.push(new MyNode(10));
linkedList.push(new MyNode(20));
console.log(linkedList.printAll("nested"));
linkedList.unshift(new MyNode(0));
console.log(linkedList.printAll());
