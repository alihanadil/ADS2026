# self-made heap
n = int(input())
h = []
def push(heap, x):
    heap.append(x)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] > heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
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
            if smallest == i:
                break 
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest 
    return top
for i in map(int, input().split()):
    push(h, i)
total = 0
while len(h) > 1:
    x = pop(h)
    y = pop(h)
    s = x + y
    total += s 
    push(h, s)
print(total)

# heapq
import heapq as hq 
n = int(input())
h = list(map(int, input().split()))
hq.heapify(h)
total = 0
while len(h) > 1:
    x = hq.heappop(h)
    y = hq.heappop(h)
    s = x + y 
    total += s 
    hq.heappush(h, s)
print(total)