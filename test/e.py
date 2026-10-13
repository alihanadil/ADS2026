# self-made heap
n, m = map(int, input().split())
h = []
s = 0
def push(heap, x):
    heap.append(x)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] > heap[i]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent 
        else:
            break 
def pop(heap):
    top = heap[0]
    last = heap.pop()
    if heap:
        heap[0] = last 
        i = 0
        n = len(heap) 
        while True:
            l = 2*i + 1
            r = l + 1
            smallest = i 
            if l < n and heap[l] < heap[smallest]:
                smallest = l 
            if r < n and heap[r] < heap[smallest]:
                smallest = r
            if i == smallest:
                break 
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest 
    return top 

for i in range(n):
    comms = input().split()
    if comms[0] == "insert":
        if len(h) < m:
            s += int(comms[1])
            push(h, int(comms[1]))
        else:
            if h[0] < int(comms[1]):
                s -= pop(h)
                push(h, int(comms[1]))
                s += int(comms[1])
    else:
        print(s)

# heapq 
import heapq as hq 
n, m = map(int, input().split())
h = []
s = 0
for i in range(n):
    comms = input().split()
    if comms[0] == "insert":
        if len(h) < m:
            s += int(comms[1])
            hq.heappush(h, int(comms[1]))
        else:
            if h[0] < int(comms[1]):
                s -= hq.heappop(h)
                hq.heappush(h, int(comms[1]))
                s += int(comms[1])
    else:
        print(s)