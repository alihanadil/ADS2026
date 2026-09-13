class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
n, k = list(map(int, input().split()))

words = LinkedList()
for i in input().split():
    new = Node(i)
    if words.head is None:
        words.head = new
        tail = words.head
        continue
    tail.next = new
    tail = tail.next
cnt = 0
current = words.head
while cnt < k:
    cnt += 1
    tail.next = current
    words.head = current.next
    current = current.next
    tail = tail.next
tail.next = None
ptr = words.head
while ptr is not None:
    print(ptr.data, end=" ")
    ptr = ptr.next