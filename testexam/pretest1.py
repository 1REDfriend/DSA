# 
# Easy stack
# 

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack :
    def __init__(self):
        self.root = None

    def push(self, data) :
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node

    def pop(self) :
        if not self.root:
            return None
        popped_node = self.root
        self.root = self.root.next
        return popped_node.data
