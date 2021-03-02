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

    def get_inorder_successor(self,node,val):
        if self is None:
            return None
        stack = []
        curr = node
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) > 0:
                    curr = stack.pop()
                    if curr.data > val:
                        return curr.data
                    curr = curr.right
                else:
                    break
        return None

root = Node(20)
root.insert(22)
root.insert(8)
root.insert(12)
root.insert(4)
root.insert(10)
root.insert(14)



root.print_list_inorder_iterative(root)
print(root.get_inorder_successor(root,10))