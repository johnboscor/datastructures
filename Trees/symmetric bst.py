class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_list_inorder_iterative(self,node):
        if self is None:
            return None
        stack = []
        res = []
        curr = node
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) > 0:
                    curr = stack.pop()
                    res.append(curr.data)
                    curr = curr.right
                else:
                    break
        print("In-order Iterative: ",res)

def check(left,right):
    if left is None and right is None:
        return True
    if left is not None and right is not None:
        return (left.data == right.data) and check(left.left,right.right) and check(left.right,right.left)
    return False

def isSymmetric(root):
    if root is None:
        return True
    return check(root.left,root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
root.print_list_inorder_iterative(root)

print(isSymmetric(root))