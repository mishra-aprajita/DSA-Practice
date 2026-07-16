class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # Left child
        self.right = None  # Right child

# Creating the tree structure
root = Node("A")
root.left = Node("B")
root.right = Node("C")

# The tree now looks like this:
#     A
#    / \
#   B   C