class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_list_preorder(self,node):
        if node:
            print(node.data, end = " ")
            self.print_list_preorder(node.left)
            self.print_list_preorder(node.right)

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


def sortedArrayToBST(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])

    return root

arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBST(arr)
root.print_list_preorder(root)
print("")
root.print_list_inorder(root)
print("")
root.print_list_postorder(root)
