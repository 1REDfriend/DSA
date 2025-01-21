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

    def delete(self, data):
        deleted, self.root = self._delete(self.root, data)
        return deleted

    def _delete(self, root, data):
        if not root:
            print("Delete Error, %s is not found in Binary Search Tree." % data)
            return None, root

        if data < root.data:
            deleted, root.left = self._delete(root.left, data)
            return deleted, root
        elif data > root.data:
            deleted, root.right = self._delete(root.right, data)
            return deleted, root
        else:
            if not root.left and not root.right:
                return root.data, None
            if not root.right:
                return root.data, root.left
            if not root.left:
                return root.data, root.right

            max_left = self.find_max(root.left)
            root.data = max_left
            deleted, root.left = self._delete(root.left, max_left)
            return data, root


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
        print()

    def find_min(self,root=None) :
        if root :
            current = root
        else :
            current = self.root
        while current.left :
            current = current.left
        return current.data

    def find_max(self,root=None) :
        if root :
            current = root
        else :
            current = self.root
        while current.right :
            current = current.right
        return current.data

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()