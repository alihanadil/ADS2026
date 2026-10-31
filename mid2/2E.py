class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
class LinkedList:
    def __init__(self):
        self.head = None 
n = int(input()) // 2
lst = LinkedList()
tail = None 
for i in map(int, input().split()):
    if lst.head is None:
        lst.head = Node(i)
        tail = lst.head 
        continue
    tail.next = Node(i)
    tail = tail.next 
prev = lst.head
curr = prev.next
cnt = 0 
while curr is not None:
    cnt += 1
    if cnt == n:
        prev.next = curr.next 
        break 
    curr = curr.next
    prev = prev.next
ptr = lst.head if cnt != 0 else None
while ptr is not None:
    print(ptr.data, end=" ")
    ptr = ptr.next