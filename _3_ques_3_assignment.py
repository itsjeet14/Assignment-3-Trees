"""Perform Pre-order, Post-order, In-order traversal"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("The value already exists in the tree.")
    
    def preorder(self):
        if self.root is not None:
            self._preorder(self.root)
    
    def _preorder(self, current_node):
        if current_node is not None:
            print(str(current_node.data))
            self._preorder(current_node.left)
            self._preorder(current_node.right)
    
    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)
    
    def _inorder(self, current_node):
        if current_node is not None:
            self._inorder(current_node.left)
            print(str(current_node.data))
            self._inorder(current_node.right)
    
    def postorder(self):
        if self.root is not None:
            self._postorder(self.root)
    
    def _postorder(self, current_node):
        if current_node is not None:
            self._postorder(current_node.left)
            self._postorder(current_node.right)
            print(str(current_node.data))

if __name__ == '__main__':
    tree = BinaryTree()
    values = input("Enter values to insert into binary tree (comma-separated): ")
    for value in values.split(','):
        tree.insert(int(value))
    
    print("Pre-order traversal:")
    tree.preorder()
    
    print("In-order traversal:")
    tree.inorder()
    
    print("Post-order traversal:")
    tree.postorder()
