class SinglyLinkedList:
    def __init__(self):
        self.tail = None
    def append(self, data):
        node = Node(data)
        if self.tail==None:
            self.tail = node
        else:
            current = self.tail
        while current.next:
            current = current.next
            current.next = node

