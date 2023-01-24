import 'package:for_dart/data-structure/linked_list.dart';
import 'package:for_dart/model/node.dart';

void main(List<String> arguments) {
  var linkedList = LinkedList();
  linkedList.push(Node(value: 10));
  linkedList.push(Node(value: 20));
  linkedList.push(Node(value: 30));
  linkedList.printAll(PrintType.arrow);
  linkedList.unShift(Node(value: 0));
  linkedList.unShift(Node(value: 50));
  linkedList.printAll();
  print('Pop: ${linkedList.pop()}');
  linkedList.printAll();
  print('Shift: ${linkedList.shift()}');
  linkedList.printAll();
}
