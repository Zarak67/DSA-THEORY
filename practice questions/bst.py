class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def delete_node(root, key):
    if root is None:
        return root
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = min_value_node(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)
    return root

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root = delete_node(root, 50)
print("Root after deletion:", root.value)
