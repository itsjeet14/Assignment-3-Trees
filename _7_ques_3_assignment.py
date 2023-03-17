"""Find sum of all nodes of the given perfect binary tree"""

# Sum of all nodes in a perfect binary tree using user input

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_of_nodes(root):
    if not root:
        return 0
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)

# User input for perfect binary tree
n = int(input("Enter the number of levels in the perfect binary tree: "))
root = Node(int(input("Enter the value of the root node: ")))

for i in range(2, n+1):
    curr_level_nodes = [root]
    for j in range(i-1):
        parent = curr_level_nodes.pop(0)
        parent.left = Node(int(input("Enter the left child value of " + str(parent.val) + ": ")))
        parent.right = Node(int(input("Enter the right child value of " + str(parent.val) + ": ")))
        curr_level_nodes.append(parent.left)
        curr_level_nodes.append(parent.right)

# Compute and print the sum of all nodes
sum = sum_of_nodes(root)
print("Sum of all nodes:", sum)
