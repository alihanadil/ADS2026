# self-made heap
n, m = map(int, input().split())
h = []
total = 0
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
for i in map(int, input().split()):
    push(h, -i)
cnt = 0 
while cnt < m:
    x = -pop(h)
    total += x 
    push(h, -(x - 1))
    cnt += 1
print(total)

# heapq
import heapq as hq
n, m = map(int, input().split())
h = []
total = 0
for i in map(int, input().split()):
    hq.heappush(h, -i)
cnt = 0
while cnt < m:
    x = -hq.heappop(h)
    total += x 
    hq.heappush(h, -(x - 1))
    cnt += 1
print(total)