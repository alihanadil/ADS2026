class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

n = int(input())
lst = LinkedList()
tail = None
count = 0
for i in range(n):
    new_node = Node(input())
    if not lst.head:
        lst.head = new_node
        tail = lst.head
        continue
    tail.next = new_node
    tail = tail.next
prev = lst.head
current = prev.next
while current is not None:
    if prev.data == current.data:
        prev.next = current.next
        current = current.next
    else:
        prev = prev.next
        current = current.next

ptr = lst.head
while ptr is not None:
    count += 1
    ptr = ptr.next
ptr = lst.head
print(count)
while ptr is not None:
    print(ptr.data)
    ptr = ptr.next