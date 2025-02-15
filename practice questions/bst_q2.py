class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1

root = Node(50)
root.left = Node(30)
root.right = Node(70)
print("Height of the tree:", height(root))
