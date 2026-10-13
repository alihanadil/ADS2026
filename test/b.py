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
            if i == smallest:
                break 
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
    return top
for i in map(int, input().split()):
    push(h, -i)
while len(h) > 1:
    x = pop(h)
    y = pop(h)
    s = abs(y - x)
    if s != 0:
        push(h, -s)
print(-h[0] if h else 0)

# heapq
import heapq as hq 
n = int(input())
h = []
hq.heapify(h)
for i in map(int, input().split()):
    hq.heappush(h, -i)
while len(h) > 1:
    x = hq.heappop(h)
    y = hq.heappop(h)
    s = abs(y - x)
    if s != 0:
        hq.heappush(h, -s)
print(-h[0] if h else 0)