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

    def is_empty(self):
        return self.head is None

    def show_detail(self):
        currentNode = self.head
        result = ""
        while currentNode:
            result += currentNode.data
            if currentNode.next:
                result += ", "
            currentNode = currentNode.next
        return result


if __name__ == "__main__":
    groups = Students()
    nameList = Students()

    groupCount = int(input())
    allStudentCount = int(input())

    for _ in range(groupCount):
        groups.push(Students())

    for _ in range(allStudentCount):
        nameList.push(input())

    current_group = groups.head
    while not nameList.is_empty():
        if not current_group:
            current_group = groups.head
        current_group.data.push(nameList.pop().data)
        current_group = current_group.next

    current_group = groups.head
    group_number = 1
    while current_group:
        print(f"Group {group_number}: {current_group.data.show_detail()}")
        group_number += 1
        current_group = current_group.next
