class Node:
    def __init__(self):
        self.key = 0
        self.parent = None
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

def insert(tree, key):
    new = Node()
    new.key = key
    treeNode = tree.root
    parent = None

    while (treeNode is not None):
        parent = treeNode
        if (treeNode.key > new.key):
            treeNode = treeNode.left
        else:
            treeNode = treeNode.right
    new.parent = parent
    if (parent == None):
        tree.root = new
    elif (new.key < parent.key):
        parent.left = new
    else:
        parent.right = new

def search(tree, key):
    treeNode = tree.root
    while (treeNode is not None):
        if (key == treeNode.key):
            return treeNode
        elif (key < treeNode.key):
            treeNode = treeNode.left
        else:
            treeNode = treeNode.right
    return None
    
def transplant(tree, u, v):
    if (u.parent == None):
        tree.root = v
    elif (u == u.parent.left):
        u.parent.left = v
    else:
        u.parent.right = v
    if (v is not None):
        v.parent = u.parent

def tree_min(node):
    while (node.left is not None):
        node = node.left
    return node

def tree_max(node):
    while (node.right is not None):
        node = node.right
    return node

def delete(tree, node):
    if (node.left == None):
        transplant(tree, node, node.right)
    elif (node.right == None):
        transplant(tree, node, node.left)
    else:
        y = tree_min(node.right)
        if (y.parent != node):
            y.right = node.right
            y.right.parent = y
        transplant(tree, node, y)
        y.left = node.left
        y.left.parent = y

def height(tree):
    def height_recur(node):
        if not node:
            return 0
        return 1 + max(height_recur(node.left), height_recur(node.right))

    return height_recur(tree.root)
def correct_check(node, mini, maxi):
    if node == None:
        return True
    if node.key < mini or node.key > maxi:
        return False
    return correct_check(node.left, mini, node.key) and correct_check(node.right, node.key, maxi)

def is_correct_bst(tree):
    return correct_check(tree.root, float("-Infinity"), float("Infinity"))
