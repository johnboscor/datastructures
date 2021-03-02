class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self,nodes=None):
        self.head = None
        #This below code is used and helpfull if you want to add multiple nodes at once. Else not necessary
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for i in nodes:
                node.next = Node(i)
                node = node.next

    def __repr__(self):   # it just prints it in link format
        temp = self.head
        nodes = []
        while temp is not None:
            nodes.append(str(temp.data))
            temp = temp.next
        nodes.append("None")
        return "->".join(nodes)

    def printList(self): #use to print it explicetely
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def addToTop(self,data):
        if self.head is not None:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        else:
            self.head = Node(data)

    def addToEnd(self,data):
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.head = Node(data)

    def addAfter(self,data,newnode):
        if not self.head:
            raise Exception("List is empty")
        temp = self.head
        while temp is not None:
            if temp.data == data:
                tempNode = Node(newnode)
                tempNode.next = temp.next
                temp.next = tempNode
                return
            temp = temp.next
        raise Exception(f"Node to insert after - {data} not found")

    def addBefore(self,data,newnode):
        if not self.head:
            raise Exception("List is empty")
        prev = curr = self.head
        while curr is not None:
            if curr.data == data:
                tempNode = Node(newnode)
                tempNode.next = curr
                prev.next = tempNode
                return
            prev = curr
            curr = curr.next
        raise Exception(f"Node to insert Before - {data} not found")

    def deleteNode(self, data):
        if not self.head:
            raise Exception("List is empty")
        if self.head.data == data:
            self.head = self.head.next
            return
        prev = curr = self.head
        while curr is not None:
            if curr.data == data:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        raise Exception(f"Node to delete- {data} not found")

    def reverse(self):
        if not self.head:
            raise Exception("List is empty")
        if not self.head.next:
            return
        next = curr = self.head
        prev = None
        while next is not None:
            next = next.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def get_head(self):
        return self.head

    def print_reverse_recursive(self,A):
        if A == None:
            return
        self.print_reverse_recursive(A.next)
        print(A.data)
    def reverse_recursion(self,A):
        if A is None:
            return
        if A.next is None:
            self.head = A
            return
        self.reverse_recursion(A.next)
        A.next.next = A
        A.next = None



#Creating a new lis
list1 = LinkedList()
node1 = Node(10)

#Adding nodes to ll.
list1.head = node1
node2 = Node(20)
node3 = Node(30)
node1.next=node2
node2.next=node3
list1.printList()
print(list1)

list2 = LinkedList(['A','B','C'])
print(list2)
list2.addToTop('0')
print(list2)
list2.addToEnd('D')
print(list2)
list2.addAfter('C','E')
print(list2)
list2.addBefore('C','F')
print(list2)
list2.deleteNode('0')
print(list2)
list2.reverse()
print(list2)
list2.reverse()
print(list2)
print("***recursive***")
head = list2.get_head()
#list2.print_reverse_recursive(head)
list2.reverse_recursion(head)
print(list2)