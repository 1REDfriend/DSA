class Node :
    def __init__(self, data: int=0):
        self.data = data
        self.left = None
        self.right = None
        self.prev = None

class BST :
    def __init__(self):
        self.root = None

    def is_empty(self) :
        return self.root is None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if data < current.data:
                if not current.left:
                    current.left = new_node
                    return
                current = current.left
            elif data > current.data:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right
            else:
                return

    def delete(self, data) :
        pass

    def preorder(self, root) :
        if root :
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root) :
        if root :
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)


    def postorder(self, root) :
        if root :
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")

    def traverse(self) :
        if not self.root :
            print("This is an empty binary search tree.")
            return

        print("Preorder: " , end='')
        self.preorder(self.root)
        print()
        print("Inorder: " , end='')
        self.inorder(self.root)
        print()
        print("Postorder: " , end='')
        self.postorder(self.root)

    def findMin(self) :
        pass

    def findMax(self) :
        pass

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()

main()