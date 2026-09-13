class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
n = int(input()) // 2
tail = None
lst = LinkedList()
for i in list(map(int, input().split())):
    new = Node(i)
    if not lst.head:
        lst.head = new
        tail = lst.head
        continue
    tail.next = new
    tail = tail.next
cnt = 0
prev = lst.head
current = prev.next
while current is not None:
    cnt += 1
    if cnt == n:
        prev.next = current.next
        break
    prev = prev.next
    current = current.next
    
if cnt == 0:
    lst.head = None
ptr = lst.head
while ptr is not None:
    print(ptr.data, end=" ")
    ptr = ptr.next