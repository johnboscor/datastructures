#https://www.interviewbit.com/problems/root-to-leaf-paths-with-sum/

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.rright is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=' ')
            self.inorder(node.right)

    def path_sum(self,node,sum,arr):
        curr_sum = sum - node.data
        if curr_sum < 0:
            return

        if node.left is None and node.right is None:
            if curr_sum == 0:
                final_arr.append(arr + [node.data])
            return
        if node.left:
            self.path_sum(node.left,curr_sum,arr + [node.data])
        if node.right:
            self.path_sum(node.right,curr_sum,arr+[node.data])





root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.left = Node(5)
root.right.right.right = Node(1)

root.inorder(root)
print("")
print("Path Sum to from leaf")
leaf_arr = []
final_arr = []
ret = root.path_sum(root, 22,[])
print(final_arr)
