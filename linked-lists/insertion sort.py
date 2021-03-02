class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

    def __repr__(self):
        return self.data

class ListNode:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            list_nodes = Node(nodes.pop(0))
            self.head = list_nodes
            for i in nodes:
                list_nodes.next = Node(i)
                list_nodes = list_nodes.next

    def __repr__(self):
        list_nodes = []
        head = self.head
        while head is not None:
            list_nodes.append(str(head.data))
            head = head.next
        list_nodes.append("None")
        return '->'.join(list_nodes)

    def get_head(self):
        return self.head

    def insert_element(self, sorted,new_node):
        if sorted is None or sorted.data >= new_node.data:
            new_node.next = sorted
            sorted = new_node

        else:
            curr = sorted
            while curr.next is not None and curr.next.data < new_node.data:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        return sorted

    def insertionSort(self):
        curr = self.head
        if curr is None or curr.next is None:
            return

        sorted_list = None
        while curr is not None:
            next = curr.next
            sorted_list = self.insert_element(sorted_list,curr)
            curr = next
        self.head = sorted_list

list1=ListNode(['1','9','4','7','5','3','4'])
print(list1)
list1.insertionSort()
print(list1)

ll = []
if