from sll import SinglyLinkedList
from node_cl import Node

class CircularSinglyLinkedList(SinglyLinkedList):
    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.size +=1
