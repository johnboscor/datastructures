def print_post_order(inorder,preorder,n):
    if preorder[0] in inorder:
        root_index = inorder.index(preorder[0])
    #print left subtree
    if root_index != 0:
        print_post_order(inorder[:root_index],preorder[1:root_index+1],len(inorder[:root_index]))
    #print right subtree
    if root_index != n -1:
        print_post_order(inorder[root_index+1:], preorder[root_index + 1:], len(inorder[root_index+1:]))

    print(preorder[0]," ",end=" ")

inorder = [96, 97, 98, 99, 100, 102]
preorder = [100, 98, 96, 97, 99, 102]

n = len(inorder)
print_post_order(inorder,preorder,n)