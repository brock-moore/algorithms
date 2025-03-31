class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_tree(vals, initVal):
    tree = BinaryNode(initVal)
    for val in vals:
        tree = insert(tree, val)
    return tree

def insert(tree, val):
    if tree is None:
        return BinaryNode(val)
    if tree.val == val:
        return tree
    if val < tree.val:
        tree.left = insert(tree.left, val)
    else:
        tree.right = insert(tree.right, val)
    return tree

def search(tree, val): 
    if tree is None:
        return False
    if val == tree.val:
        return True
    if val < tree.val:
        return search(tree.left, val)
    else:
        return search(tree.right, val)

def order_traversal(tree):
    if tree is None:
        return
    order_traversal(tree.left)
    print(tree.val, end=" ")
    order_traversal(tree.right)

tree = create_tree([5,3,9,2,4,2,12,-3,60], 6)

order_traversal(tree)
print()
print(search(tree, 3))
print(search(tree, 7))

insert(tree, 7)
order_traversal(tree)
print()
print(search(tree, 7))