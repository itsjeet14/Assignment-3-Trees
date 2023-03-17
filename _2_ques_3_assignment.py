"""Find height of a given tree"""

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
    
    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root)
    
    def _height(self, current_node):
        if current_node is None:
            return 0
        else:
            left_height = self._height(current_node.left)
            right_height = self._height(current_node.right)
            return max(left_height, right_height) + 1

if __name__ == '__main__':
    tree = BinaryTree()
    values = input("Enter values to insert into binary tree (comma-separated): ")
    for value in values.split(','):
        tree.insert(int(value))
    
    print("Height of the binary tree is:", tree.height())
