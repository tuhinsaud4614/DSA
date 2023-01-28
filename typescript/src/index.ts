import { LinkedList } from "data-structure";

const linkedList = new LinkedList();
linkedList.push(10);
linkedList.push(20);
linkedList.push(30);
linkedList.unshift(0);
linkedList.unshift(50);
linkedList.printAll();
console.log("Pop:", linkedList.pop());
linkedList.printAll();
console.log(linkedList.size);

console.log("Shift:", linkedList.shift());
linkedList.printAll();
linkedList.insertAt(100, 0);
linkedList.printAll();
console.log(linkedList.size);

