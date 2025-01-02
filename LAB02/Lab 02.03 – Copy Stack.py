class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Students:
    def __init__(self):
        self.head = None

    def push(self, value=""):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode

    def pop(self):
        if not self.head:
            return None
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

    def print_stack(self):
        currentNode = self.head
        result = ""
        while currentNode:
            if currentNode.data.isalpha() :
                result += f"'{currentNode.data}'"
            else :
                result += currentNode.data
            if currentNode.next:
                result += ", "
            currentNode = currentNode.next
        print(f"{chr(91)}{result}{chr(93)}")

def print_status():
    """Print all stacks"""
    print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
    STACK1_.print_stack()
    print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
    STACK2_.print_stack()
    print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
    STACK3_.print_stack()
    print("This is stack 4 (%d): " % STACK4_.get_size(), end='')
    STACK4_.print_stack()
    print()

def copy_stack(stack1, stack2) :
    stack2.head = None
    current = stack1.head
    while current:
        stack2.push(current.data)
        current = current.next

STACK1_ = Students()
STACK2_ = Students()

STACK3_ = Students()
STACK4_ = Students()

# เพิ่มข้อมูลใน Stack1
for _ in range(int(input())):
    STACK1_.push(input())

# เพิ่มข้อมูลใน Stack2
for _ in range(int(input())):
    STACK2_.push(input())

TEMP1_, TEMP2_, TEMP3_, TEMP4_ = id(STACK1_), id(STACK2_), id(STACK3_), id(STACK4_)

print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
print_status()

print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("A")
print_status()

print("Copy Stack 2 to Stack 1")
copy_stack(STACK2_, STACK1_)
STACK2_.push("B")
print_status()

print("Copy Stack 3 to Stack 2")
copy_stack(STACK3_, STACK2_)
STACK3_.push("C")
print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("D")
print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
STACK2_.push("E")
print_status()

print(TEMP1_ == id(STACK1_), TEMP2_ == id(STACK2_),
    TEMP3_ == id(STACK3_), TEMP4_ == id(STACK4_))