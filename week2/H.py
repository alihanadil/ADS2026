class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None    
n = int(input())

days = LinkedList()
for i in list(map(int, input().split())):
    new = Node(i)
    if days.head is None:
        days.head = new
        tail = days.head
        continue    
    tail.next = new
    tail = tail.next
sum = 0
max = 0
worst = -999999
current = days.head
while current is not None:
    sum += current.data
    # print(sum, end=", ")
    if sum < 0:
        sum = 0
    elif sum > max:
        max = sum
    if worst < current.data and current.data < 0:
        worst = current.data
    current = current.next
print(max if max > 0 else worst)