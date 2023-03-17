"""Count subtress that sum up to a given value x in a binary tree"""

# Count subtrees that sum up to a given value x in a binary tree using user input

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_subtrees_with_sum(root, x):
    if not root:
        return 0

    count = 0
    if root.val == x:
        count += 1

    count += count_subtrees_with_sum(root.left, x - root.val) + count_subtrees_with_sum(root.right, x - root.val)
    return count

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

# User input for the target sum
x = int(input("Enter the target sum: "))

# Compute and print the number of subtrees that sum up to the target sum
count = count_subtrees_with_sum(root, x)
print("Number of subtrees that sum up to", x, ":", count)

