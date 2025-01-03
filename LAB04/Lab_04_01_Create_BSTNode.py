class BTSNode :
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class SinglyLinked :
    def __init__(self):
        self.head = None

    def push(self, data='') :
        new_node = BTSNode(data)
        if not self.head :
            self.head = new_node

        current = self.head
        while current :
            current = current.right
        current = new_node



ling = SinglyLinked()
ling.push(input())
print(ling.head.data)
print(ling.head.left)
print(ling.head.right)
