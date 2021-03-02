class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def __repr__(self):
        return self.data

class QueueList:
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

    def enqueue(self,val):
        if self.head is not None:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
        else:
            self.head = Node(val)

    def dequeue(self):
        if self.head is None:
            raise Exception("Queue is empty")
        else:
            curr = self.head
            prev = None
            while curr.next is not None:
                prev = curr
                curr = curr.next
            val = curr.data
            if prev is None:
                self.head = None
            else:
                prev.next = None
        return val

queue1 = QueueList()
queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)
print(queue1)
print(queue1.dequeue())
print(queue1)
print(queue1.dequeue())
print(queue1)
print(queue1.dequeue())
print(queue1)


