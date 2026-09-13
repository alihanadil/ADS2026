class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
lst = DoublyLinkedList()
while True:
    try:
        parts = input().split()
        if parts[0] == "add_front":
            print("ok")
            if lst.head is None:
                lst.head = Node(parts[1])
                lst.tail = lst.head
                continue
            old_head = lst.head
            lst.head = Node(parts[1])
            lst.head.prev = None
            lst.head.next = old_head
            old_head.prev = lst.head
        elif parts[0] == "add_back":
            print("ok")
            if lst.head is None:
                lst.tail = Node(parts[1])
                lst.head = lst.tail
                continue
            old_tail = lst.tail
            lst.tail = Node(parts[1])
            lst.tail.prev = old_tail
            lst.tail.next = None
            old_tail.next = lst.tail
        elif parts[0] == "erase_front":
            if lst.head is None:
                print("error")
                continue
            print(lst.head.data)
            if lst.head == lst.tail:
                lst.head = lst.tail = None
                continue
            lst.head = lst.head.next
            lst.head.prev = None
        elif parts[0] == "erase_back":
            if lst.tail is None:
                print("error")
                continue
            print(lst.tail.data)
            if lst.head == lst.tail:
                lst.head = lst.tail = None
                continue
            lst.tail = lst.tail.prev
            lst.tail.next = None
        elif parts[0] == "front":
            if lst.head is None:
                print("error")
                continue
            print(lst.head.data)
        elif parts[0] == "back":
            if lst.tail is None:
                print("error")
                continue
            print(lst.tail.data)
        elif parts[0] == "clear":
            lst.head = None
            lst.tail = None
            print("ok")
        elif parts[0] == "exit":
            print("goodbye")
            break
    except EOFError:
        break