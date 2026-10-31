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
curr = lst.head 
prev = None
while curr is not None:
    temp = curr.next 
    curr.next = prev 
    prev = curr 
    curr = temp
ptr = prev 
while prev is not None:
    print(prev.data, end=" ")
    prev = prev.next