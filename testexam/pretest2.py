# 
# singly linked list
# 

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class Sglylist :
    def __init__(self):
        self.root = None

    def insert(self, data) :
        new_node = Node(data)
        current = self.root
        if not current :
            self.root = new_node
            return

        while current.next :
            current = current.next

        current.next = new_node

    def pop(self) :
        if not current :
            return None

        if not self.root.next:
            pop_data = self.root.data
            self.root = None
            return pop_data

        current = self.root

        while current.next.next:
            current = current.next

        pop_data = current.next.data
        current.next = None
        return pop_data

    def insert_before(self, find, data) :
        new_node = Node(data)
        current = self.root
        prev = None

        if not current :
            return

        if current.data == find:
            new_node.next = self.root
            self.root = new_node
            return

        while current :
            if current.data == find :
                temp_node = Node(current)
                prev.next = new_node
                prev.next.next = temp_node
            prev = current
            current = current.next


    def delete(self, data) :
        current = self.root
        prev = None

        if not current :
            return None

        if current.data == data:  # ลบโหนดแรก
            self.root = current.next
            return

        while current :
            if current.data == data :
                prev.next = current.next
                return
            prev = current
            current = current.next

