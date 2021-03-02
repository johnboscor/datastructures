
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_in_order(root):
    if root is None:
        return None
    print_in_order(root.left)
    print(root.data,end=' ')
    print_in_order(root.right)

def print_post_order(root):
    if root is None:
        return None
    print_in_order(root.left)
    print_in_order(root.right)
    print(root.data, end=' ')

def buildTree(preorder,inorder):
    if inorder is None:
        return None
    root = Node(preorder[0])
    root_i = inorder.index(preorder[0])
    if root_i != 0:
        root.left = buildTree(preorder[1:root_i+1],inorder[:root_i])
    if root_i != len(inorder) - 1:
        root.right = buildTree(preorder[root_i+1:],inorder[root_i+1:])
    return root


inorder = [96, 97, 98, 99, 100, 102]
preorder = [100, 98, 96, 97, 99, 102]

root=buildTree(preorder,inorder)
print_in_order(root)
print("")
print_post_order(root)