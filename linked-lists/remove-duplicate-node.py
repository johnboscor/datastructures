class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data

class double_LL:
    def __init__(self,data=None):
        self.head = None
        if data is not None:
            self.head = Node(int(data.pop(0)))
        temp = self.head
        for i in data:
            temp.next = Node(int(i))
            temp.next.prev = temp
            temp = temp.next

    def __repr__(self):
        if self.head is None:
            return None
        lst = []
        node = self.head
        lst.append("None")
        while node is not None:
            lst.append(str(node.data))
            node = node.next
        lst.append("None")
        return "<->".join(lst)

    def deleteDuplicate(self):
        lst = []
        temp = self.head
        if temp is None:
            return

        while temp is not None:
            if temp.data in lst:
                print("Duplicate found: ",temp.data)
                temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                temp = temp.next
            else:
                lst.append(temp.data)
                temp = temp.next


newlist = double_LL(['4','5','3','2','4','7','1','5'])
print("Linked list - original: ",newlist)
newlist.deleteDuplicate()
print("Linked list - after deleting duplicate: ",newlist)

