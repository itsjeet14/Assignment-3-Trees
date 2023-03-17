"""Implement Binary tree"""

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
    
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
    
    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left)
            print(str(current_node.data))
            self._print_tree(current_node.right)

if __name__ == '__main__':
    tree = BinaryTree()
    values = input("Enter values to insert into binary tree (comma-separated): ")
    for value in values.split(','):
        tree.insert(int(value))
    
    tree.print_tree()
