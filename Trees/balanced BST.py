class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
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

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def isTreeBalanced(root):
    if root is None:
        return True

    lh = height(root.left)
    rh = height(root.right)

    if abs(lh-rh) <=1 and isTreeBalanced(root.left) and isTreeBalanced(root.right):
        return True

    return False



root = Node(100)
root.insert(102)
root.insert(98)
root.insert(99)
root.insert(96)
root.insert(97)
#root.insert(105)



root.print_list_inorder_iterative(root)
print(isTreeBalanced(root))

