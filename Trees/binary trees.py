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

    def findMin(self,root):
            while root.left is not None:
                root = root.left
            return root

    def delete(self, root,data):
        if root is None:
            return None

        if data < root.data:
            root.left = root.delete(root.left, data)
        elif data > root.data:
            root.right = root.delete(root.right, data)
        else:
            if root.left is None and root.right is None:
                root = None
                return root
            elif root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.right
                root = None
                return root.left
            else:
                temp_min = root.findMin(root.right)
                root.data = temp_min.data
                root.right = root.delete(root.right,temp_min.data)
        return root

    def print_list_preorder(self, node):
        if node:
           print(node.data, end = " ")
           self.print_list_preorder(node.left)
           self.print_list_preorder(node.right)

    def print_list_preorder_iterative(self,node):
        if self is None:
            return None
        stack = []
        res = []
        curr = node
        stack.append(curr)
        res.append(curr.data)
        curr = curr.left
        while True:
            if curr is not None:
                stack.append(curr)
                res.append(curr.data)
                curr = curr.left
            else:
                if len(stack) > 0:
                    curr = stack.pop()
                    curr = curr.right
                else:
                    break
        print("Pre-order Iterative: ",res)

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

    def print_list_postorder_iterative(self,node):
        if self is None:
            return None
        stack = [node]
        res = []
        while stack:
            temp = stack.pop()
            res.append(temp.data)
            if temp.left: stack.append(temp.left)
            if temp.right: stack.append(temp.right)
        print("Post-order Iterative: ", res[::-1])

    def print_list_inorder(self,node):
        if node:
            self.print_list_inorder(node.left)
            print(node.data, end = " ")
            self.print_list_inorder(node.right)


    def print_list_postorder(self, node):
        if node:
           self.print_list_postorder(node.left)
           self.print_list_postorder(node.right)
           print(node.data,end = " ")

    def print_list_level_order(self,node):
        print("Level order Iterative:")
        if node is None:
            return None
        queue = []
        queue.append(node)
        while queue:
            curr = queue.pop()
            print(curr.data,end = " ")
            if curr.left: queue = [curr.left] + queue
            if curr.right: queue = [curr.right] + queue

def isvalidBST(root,minval,maxval):
    if root is None:
        return True
    if root.data > minval and root.data < maxval and \
        isvalidBST(root.left,minval,root.data) and \
        isvalidBST(root.right,root.data,maxval):
        return True
    else:
        return False

root = Node(100)
root.insert(102)
root.insert(98)
root.insert(99)
root.insert(96)
root.insert(97)




root.print_list_preorder(root)
print("")
root.print_list_inorder(root)
print("")
root.print_list_postorder(root)
print("")
root.print_list_preorder_iterative(root)
root.print_list_inorder_iterative(root)
root.print_list_postorder_iterative(root)
root.print_list_level_order(root)
minval  = -2**32
maxval = 2**32
print(isvalidBST(root,minval,maxval))


#root.delete(root,3)
#root.print_list_inorder_iterative(root)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,data):
        self.head
