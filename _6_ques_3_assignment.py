"""Find sum of all left leaves in a given Binary Tree"""

# Sum of all left leaves in a binary tree using user input

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    if not root:
        return 0

    sum = 0
    if root.left and not root.left.left and not root.left.right:
        sum += root.left.val

    sum += sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)
    return sum

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

# Compute and print the sum of all left leaves
sum = sum_of_left_leaves(root)
print("Sum of all left leaves:", sum)
