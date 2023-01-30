import 'package:for_dart/data-structure/linked_list.dart';

void main(List<String> arguments) {
  var linkedList = LinkedList<int>();
  linkedList.push(1);
  linkedList.push(2);
  linkedList.push(3);
  linkedList.printAll();
  linkedList.unShift(0);
  linkedList.unShift(-1);
  linkedList.printAll();
  print('Size: ${linkedList.size}');
  print('Pop: ${linkedList.pop()}');
  print('Size: ${linkedList.size}');
  linkedList.printAll();
  print('Shift: ${linkedList.shift()}');
  print('Size: ${linkedList.size}');
  linkedList.printAll();
  linkedList.insertAt(-2, 1);
  print('Size: ${linkedList.size}');
  linkedList.printAll();
}
