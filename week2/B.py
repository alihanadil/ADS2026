class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # The list starts empty
    # Insert a node at the end of the list (Time Complexity: O(n))
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

n = int(input())
lst = LinkedList()
for i in input().split():
    lst.append(i)
prev = lst.head
current = prev.next
    
while current is not None:
    prev.next = current.next
    if current.next is None:
        break
    current = current.next.next
    prev = prev.next

ptr = lst.head
while ptr is not None:
    print(ptr.data, end=" ")
    ptr = ptr.next
