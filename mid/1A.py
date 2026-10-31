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
k = int(input())
while lst.head is not None and lst.head.data == k:
    lst.head = lst.head.next
prev = lst.head
curr = prev.next
while curr is not None:
    if curr.data == k:
        prev.next = curr.next 
    else:
        prev = prev.next 
    curr = curr.next
ptr = lst.head 
while ptr is not None:
    print(ptr.data, end=" ")
    ptr = ptr.next 