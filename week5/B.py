# heapq version
import heapq
n = int(input())
h = [-n for n in map(int, input().split())]
heapq.heapify(h)
while(len(h) > 1):
    x = -heapq.heappop(h)
    y = -heapq.heappop(h)
    s = abs(y - x)
    if s != 0:
        heapq.heappush(h, -s)
print(-h[0] if h else 0)

# exceeds time limit
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
            left, right = 2*i + 1, 2*i + 2
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
    push(h, -i)
while(len(h) > 1):
    x = abs(pop(h))
    y = abs(pop(h))
    s = abs(y - x)
    if s != 0:
        push(h, -s)
print(-h[0] if h else 0)