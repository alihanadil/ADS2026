# self-made heap
n, m = map(int, input().split())
h = []
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
    push(h, i)
cnt = 0
possible = False
while h:
    x = pop(h)
    if x >= m:
        possible = True 
        break 
    if not h:
        break 
    y = 2 * pop(h)
    push(h, x + y)
    cnt += 1 
print(cnt if possible else -1)

# heapq
import heapq as hq 
n, m = map(int, input().split())
h = list(map(int, input().split()))
hq.heapify(h)
cnt = 0 
possible = False 
while h:
    x = hq.heappop(h)
    if x >= m:
        possible = True 
        break
    if not h:
        break
    y = 2 * hq.heappop(h)
    hq.heappush(h, x + y)
    cnt += 1
print(cnt if possible else -1)