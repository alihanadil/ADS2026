class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
n = int(input())
tail = None
lst = LinkedList()

for i in input().split():
    new = Node(i)
    if not lst.head:
        lst.head = new
        tail = lst.head
        continue
    tail.next = new
    tail = tail.next
current = lst.head
prev = None
while current is not None:
    temp = current.next
    current.next = prev
    prev = current
    current = temp

ptr = prev
while ptr is not None:
    print(ptr.data, end=" ")
    ptr = ptr.next