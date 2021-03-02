# https://www.interviewbit.com/problems/add-two-numbers-as-lists/

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, list=None):
        self.head = None
        if list is not None:
            self.head = Node(int(list.pop(0)))
            node = self.head
            while len(list) > 0:
                node.next = Node(int(list.pop(0)))
                node = node.next

    def __repr__(self):
        if self.head is None:
            return None
        node = self.head
        lst = []
        while node is not None:
            lst.append(str(node.data))
            node = node.next
        lst.append("None")
        return '->'.join(lst)


def print_list(root):
    while root is not None:
        print(root.data, end=' ')
        root = root.next


def addLists(L1, L2):
    if L1 is None: return L2
    if L2 is None: return L1

    res = Node(-1)
    dummy = res
    sum_val = 0
    carry = 0
    while L1 is not None and L2 is not None:
        val1 = L1.data if L1 is not None else 0
        val2 = L2.data if L2 is not None else 0
        sum_val = val1 + val2 + carry
        carry = sum_val // 10
        sum_val %= 10
        res.next = Node(sum_val)
        res = res.next

        L1 = L1.next if L1.next is not None else None
        L2 = L2.next if L2.next is not None else None
    if carry > 0:
        res.next = Node(carry)
    return dummy.next


# L1 = LinkedList(['2','4','3'])
# L2 = LinkedList(['5','6','4'])
# print(L1)
# print(L2)
L1 = Node(9)
L1.next = Node(4)
L1.next.next = Node(1)

L2 = Node(5)
L2.next = Node(6)
L2.next.next = Node(8)
print_list(L1)
print("")
print_list(L2)
print("")
sum_list = addLists(L1,L2)
print_list(sum_list)
