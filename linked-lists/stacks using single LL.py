class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def __repr__(self):
        return self.data


class StackList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        temp = self.head
        nodes = []
        while temp is not None:
            nodes.append(str(temp.data))
            temp = temp.next
        nodes.append("None")
        return "->".join(nodes)

    def pushVal(self, val):
        if self.head is not None:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
        else:
            self.head = Node(val)

    def popVal(self):
        if self.head is None:
            raise Exception("Stack is empty, nothing to pop!")
        else:
            temp = self.head.data
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head = None
        return temp


stack1 = StackList()
stack1.pushVal(10)
stack1.pushVal(20)
stack1.pushVal(30)
print(stack1)
print(stack1.popVal())
print(stack1)
print(stack1.popVal())
print(stack1)
