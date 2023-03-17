"""Find maximum level sum in Binary Tree"""

# Find maximum level sum in Binary Tree using user input

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_level_sum(root):
    if not root:
        return 0

    level_sum = root.val
    max_sum = level_sum
    q = [root]

    while q:
        level_sum = 0
        size = len(q)

        for i in range(size):
            node = q.pop(0)
            level_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        max_sum = max(max_sum, level_sum)

    return max_sum

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

# Compute and print the maximum level sum
max_sum = max_level_sum(root)
print("Maximum level sum:", max_sum)
