class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
m = list(map(int, input().split()))
mlst = LinkedList()
tail = None
for i in range(1, m[0] + 1):
    new = Node(m[i])
    if mlst.head is None:
        mlst.head = new
        tail = mlst.head
        continue    
    tail.next = new
    tail = tail.next
tail = None
n = list(map(int, input().split()))
nlst = LinkedList()
for i in range(1, n[0] + 1):
    new = Node(n[i])
    if nlst.head is None:
        nlst.head = new
        tail = nlst.head
        continue    
    tail.next = new
    tail = tail.next

merged = LinkedList()
# merged.head = nlst.head if (mlst.head is None) or (nlst.head.data < mlst.head.data) else mlst.head
if nlst.head and (mlst.head is None or nlst.head.data <= mlst.head.data):
    merged.head = nlst.head
    l1 = mlst.head
    l2 = nlst.head
    l2 = l2.next
elif mlst.head and (nlst.head is None or mlst.head.data <= nlst.head.data):
    merged.head = mlst.head
    l1 = mlst.head
    l1 = l1.next
    l2 = nlst.head
else:
    merged.head = None
    l1 = None
    l2 = None
tail_m = merged.head if merged.head else None
while l1 is not None or l2 is not None:
    if l1 is None:
        tail_m.next = l2
        tail_m = tail_m.next
        l2 = l2.next
        continue
    elif l2 is None:
        tail_m.next = l1
        tail_m = tail_m.next
        l1 = l1.next
        continue
    if l1.data <= l2.data:
        tail_m.next = l1
        tail_m = tail_m.next
        l1 = l1.next
        continue
    else:
        tail_m.next = l2
        tail_m = tail_m.next
        l2 = l2.next
        continue

ptr = merged.head
while ptr is not None:
    print(ptr.data, end=" ")
    ptr = ptr.next