class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        temp = self.head
        nodes = []
        nodes.append("None")
        while temp is not None:
            nodes.append(str(temp.data))
            temp=temp.next
        nodes.append("None")
        return '<->'.join(nodes)

    def addToFirst(self,val):
        if self.head is None:
            self.head = Node(val)
        else:
            temp = Node(val)
            temp.next = self.head
            temp.next.prev = temp
            self.head = temp

    def addToEnd(self,val):
        if self.head is None:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            newnode = Node(val)
            newnode.prev = temp
            temp.next = newnode

    def addAfter(self,after,val):
        if self.head is None:
            raise Exception("Link list is empty")
        else:
            temp = self.head
            while temp is not None:
                if temp.data == after:
                    newnode = Node(val)
                    temp.next.prev = newnode
                    newnode.next = temp.next
                    temp.next  = newnode
                    newnode.priv=temp
                    return
                temp = temp.next
            raise Exception("Node to be inserted after not found!")

    def getHead(self):
        return self.head

    def reverse(self, A):
        if not self.head:
            raise Exception("List is empty")
        if not self.head.next:
            return
        curr = next = self.head
        prev = None
        while next is not None:
            next = next.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        self.head = prev





list1 = DoubleLinkedList()
list1.addToFirst(10)
list1.addToFirst(20)
list1.addToFirst(30)
list1.addToEnd(5)
list1.addToEnd(1)
print(list1)
list1.addAfter(10,4)
print(list1)
list1.reverse(list1.getHead())
print(list1)