class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0
    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1
    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data
class StackQueue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []
    def enqueue(self, data):
        self.inbound_stack.append(data)
    def dequeue(self,):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
                return self.outbound_stack.pop()

class Node():
    def __init__(self, data=None, post=None, prev=None):
        self.data = data
        self.post = post
        self.prev = prev
     def __str__(self):
         return str(data)

class NodeQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
