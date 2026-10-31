class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None 
n = int(input())
lst = LinkedList()
tail = None 
for i in map(int, input().split()):
    if lst.head is None:
        lst.head = Node(i)
        tail = lst.head 
        continue
    tail.next = Node(i)
    tail = tail.next 
m, k = map(int, input().split())
if m == 0:
    temp = lst.head 
    lst.head = Node(k)
    lst.head.next = temp 
else:
    curr = lst.head
    for _ in range(m - 1):
        curr = curr.next 
    temp = curr.next 
    curr.next = Node(k)
    curr = curr.next 
    curr.next = temp
ptr = lst.head 
while ptr is not None:
    print(ptr.data, end=" ")
    ptr = ptr.next