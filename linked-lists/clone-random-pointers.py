#https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):

    def copyRandomList(self, head):
        mydict = dict()

        def copy_node(node):
            if not node:
                return None
            if node in mydict:
                return mydict[node]

            newnode = Node(node.val)
            mydict[node] = newnode
            return newnode

        node = head
        while node is not None:
            new = copy_node(node)
            new.next = copy_node(node.next)
            new.random = copy_node(node.random)

        return mydict[head]