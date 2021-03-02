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

    #Do inorder traversal and return kth element...
    def kth_smallest(self,root,k):
        n = 0
        stack = []
        curr = root
        val = curr.data
        while True:
            if n == k:
                break
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) > 0:
                    curr = stack.pop()
                    val = curr.data
                    curr = curr.right
                    n += 1
                else:
                    break

        print(f"The {k}th smallest value is: {val}")

    def post_order(self,A):
        stack = [A]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.data)
            if curr.left: stack.append(curr.left)
            if curr.right: stack.append(curr.right)
        print(res[::-1])

root = Node(100)
root.insert(102)
root.insert(98)
root.insert(99)
root.insert(96)
root.insert(97)
root.post_order(root)
root.kth_smallest(root,2)