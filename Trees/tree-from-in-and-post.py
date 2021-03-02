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

def buildTree(postorder,inorder):
    if postorder is None:
        return None
    root = Node(postorder[-1])
    root_i = inorder.index(postorder[-1])
    if root_i != 0:
        root.left = buildTree(postorder[:root_i],inorder[:root_i])
    if root_i != len(inorder) - 1:
        root.right = buildTree(postorder[root_i:-1],inorder[root_i+1:])
    return root


inorder = [96, 97, 98, 99, 100, 102]
postorder = [97, 96, 99, 98, 102, 100]
#preorder = [100, 98, 96, 97, 99, 102]
root=buildTree(postorder,inorder)
print_in_order(root)
print("")
print_post_order(root)