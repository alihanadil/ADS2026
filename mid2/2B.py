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
cnt = 0
while curr is not None:
    if cnt % 2 == 0:
        print(curr.data, end=" ")
    curr = curr.next
    cnt += 1