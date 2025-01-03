class DateNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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

    def delete(self, data):
        current = self.head
        prev = None
        result = False

        while current:
            if current.data == data:
                result = True
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return result
            prev = current
            current = current.next
        
        if not result:
            print('Cannot delete, %s does not exist.' % data)
        return result

    def insert_front(self, value='') :
        current = self.head
        temp_node = DateNode(value)

        temp_node.next = current
        self.head = temp_node

    def insert_last(self, value='') :
        newNode = DateNode(value)
        if not self.head:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode

    def insert_before(self, value1 , value2) :
        new_node = DateNode(value2)
        current = self.head
        prev = None
        result = False

        while current:
            if current.data == value1:
                result = True
                new_node.next = current
                if prev:
                    prev.next = new_node
                else:
                    self.head = new_node
                return result
            prev = current
            current = current.next
        if not result :
            print('Cannot insert, %s does not exist.' %value1)
        return result

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

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()