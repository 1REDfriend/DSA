class DateNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly:
    def __init__(self):
        self.head = None

    def push(self, value=""):
        newNode = DateNode(value)
        if not self.head:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode

    def pop(self):
        if not self.head:
            print("Underflow: Cannot pop data from an empty list")
            return False
        if not self.head.next:
            temp_node = self.head
            self.head = None
            return temp_node
        currentNode = self.head
        prevNode = None
        while currentNode.next:
            prevNode = currentNode
            currentNode = currentNode.next
        prevNode.next = None
        return currentNode

    def pop_first(self):
        if not self.head:
            return None
        current_node = self.head
        self.head = self.head.next
        current_node.next = None
        return current_node

    def get_size(self) :
        count = 0
        current_node = self.head
        while current_node :
            current_node = current_node.next
            count += 1
        return count

    def is_empty(self):
        return self.head is None

    def traverse(self):
        current = self.head
        if not current :
            print("This is an empty list.")
            return None
        result = ''
        while current :
            result += current.data
            if current.next :
                result += " -> "
            current = current.next
        print(result)

    def find_stack(self, find) :
        current = self.head
        result = 0
        while current.next :
            if current.data == find :
                result += 1
            current = current.next
        return result

sg = Singly()
for _ in range(int(input())) :
    sg.push(input())
sg.traverse()