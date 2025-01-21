# 
# binary search tree
# 

class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST :
    def __init__(self):
        self.root = None

    def insert(self, data) :
        new_node = Node(data)
        current = self.root

        if not current :
            current = new_node
            return

        while True :
            if data <= current.data:  # ไปทางซ้าย
                if current.left is None:  # ถ้าไม่มีโหนดทางซ้าย
                    current.left = new_node
                    return
                current = current.left
            else:  # ไปทางขวา
                if current.right is None:  # ถ้าไม่มีโหนดทางขวา
                    current.right = new_node
                    return
                current = current.right

    def delete(self, data, root=None) :
        if root is None:
            root = self.root
            if root is None:
                return None

        if data < root.data:  # ไปทางซ้าย
            root.left = self.delete(data, root.left)
        elif data > root.data:  # ไปทางขวา
            root.right = self.delete(data, root.right)
        else:  # พบโหนดที่ต้องการลบ
            if root.left is None:  # ไม่มีลูกทางซ้าย
                return root.right
            elif root.right is None:  # ไม่มีลูกทางขวา
                return root.left
            else:  # มีลูกทั้งสองฝั่ง
                min_larger_node = self.find_min(root.right)
                root.data = min_larger_node.data
                root.right = self.delete(min_larger_node.data, root.right)

        if root == self.root :
            self.root = root

        return root

    def find_min(self) :
        current = self.root
        if not current :
            return None
        while current.left :
            current = current.left

        return current.data

    def find_max(self) :
        current = self.root
        if not current :
            return None
        while current.right :
            current = current.right

        return current.data

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

