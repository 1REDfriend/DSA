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
            print("Underflow: Cannot pop data from an empty list")
            return False
        if not self.head.next:
            temp_node = self.head
            self.head = None
            return True
        currentNode = self.head
        prevNode = None
        while currentNode.next:
            prevNode = currentNode
            currentNode = currentNode.next
        prevNode.next = None
        return True

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


    def find_stack(self, find) :
        current = self.head
        result = 0
        while current.next :
            if current.data == find :
                result += 1
            current = current.next
        return result


def is_parentheses_matching(text) :
    st = Students()
    error = True
    for i in text :
        if i == "(" :
            st.push(i)
        elif i == ")" :
            error = st.pop()

    if st.is_empty() and error:
        return True
    return False

text = input()
result = is_parentheses_matching(text)
if result :
    print(f"Parentheses in {text} are matched")
else :
    print(f"Parentheses in {text} are unmatched")
print(result)