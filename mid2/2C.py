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
cnt = 0
for i in range(n):
    if lst.head is None:
        cnt += 1
        lst.head = Node(input())
        tail = lst.head 
        continue
    a = input()
    if tail.data != a:
        cnt += 1
        tail.next = Node(a)
        tail = tail.next 
ptr = lst.head
print(cnt) 
while ptr is not None:
    print(ptr.data)
    ptr = ptr.next