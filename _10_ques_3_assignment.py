"""Print the nodes at odd levels of a tree"""

# Print the nodes at odd levels of a tree using user input

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_odd_level_nodes(root):
    if not root:
        return

    q = [root]
    level = 1

    while q:
        size = len(q)

        for i in range(size):
            node = q.pop(0)

            if level % 2 != 0:
                print(node.val, end=" ")

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        level += 1

# User input for binary tree
root = Node(int(input("Enter the root value: ")))

root.left = Node(int(input("Enter the left child value of root (or 0 if no left child): ")))
if root.left.val != 0:
    root.left.left = Node(int(input("Enter the left child value of left child (or 0 if no left child): ")))
    root.left.right = Node(int(input("Enter the right child value of left child (or 0 if no right child): ")))

root.right = Node(int(input("Enter the right child value of root (or 0 if no right child): ")))
if root.right.val != 0:
    root.right.left = Node(int(input("Enter the left child value of right child (or 0 if no left child): ")))
    root.right.right = Node(int(input("Enter the right child value of right child (or 0 if no right child): ")))

# Print the nodes at odd levels
print("Nodes at odd levels:", end=" ")
print_odd_level_nodes(root)
