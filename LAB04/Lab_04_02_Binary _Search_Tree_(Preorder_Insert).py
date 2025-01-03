class BST :
    def __init__(self):
        self.root = None

    def is_empty(self) :
        return self.root is None

    def insert(self, data) :
        current 

    def delete(self, data) :
        pass

    def preorder(self, root) :
        if (root != None):
            print("->", root.get_data(), end=" ")
            self.preorder(root.get_left())
            self.preorder(root.get_right())

    def inorder(self, root) :
        if (root != None):
            self.inorder(root.get_left())
            print("->", root.get_data(), end=" ")
            self.inorder(root.get_right())


    def postorder(self, root) :
        if (root != None):
            self.postorder(root.get_left())
            self.postorder(root.get_right())
            print("->", root.get_data(), end=" ")

    def traverse(self, data) :
        pass

    def findMin(self) :
        pass

    def findMax(self) :
        pass

