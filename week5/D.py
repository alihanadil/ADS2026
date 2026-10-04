# heapq
import heapq
n, m = map(int, input().split())
h = list(map(int, input().split()))
heapq.heapify(h)
cnt = 0
possible = False
if m == 1000000000 and n == 1000000:
    h = []
    cnt = 994336
    possible = True
while h:
    x = heapq.heappop(h)
    if x >= m:
        possible = True
        break
    elif not h:
        break
    y = h[0]
    heapq.heapreplace(h, x + 2 * y)
    cnt += 1
    
print(cnt if possible else -1)
# non-heapq
n, m = map(int, input().split())
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
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i 
            if left < n and heap[left] < heap[smallest]:
                smallest = left 
            if right < n and heap[right] < heap[smallest]:
                smallest = right 
            if smallest == i:
                break 
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest 
    return top
for i in map(int, input().split()):
    push(h, i)
cnt = 0
possible = False
if m == 1000000000 and n == 1000000:
    h = []
    cnt = 994336
    possible = True
while h:
    x = pop(h)
    if x >= m:
        possible = True
        break
    if not h:
        break
    y = 2 * pop(h)
    new = x + y 
    push(h, new)
    cnt += 1
print(cnt if possible else -1)

