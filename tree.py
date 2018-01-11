class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

# Binary search tree
class Bst:
    def __init__(self):
        self.root_node = None
    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current
