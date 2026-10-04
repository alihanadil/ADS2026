# heapq version
import heapq
n = int(input())
h = list(map(int, input().split()))
heapq.heapify(h)
total = 0
while(len(h) > 1):
    x = heapq.heappop(h)
    y = heapq.heappop(h)
    s = x + y 
    total += s 
    heapq.heappush(h, s)
print(total)

#exceeds time limit
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
    push(h, i)
total = 0
while(len(h) > 1):
    x = pop(h)
    y = pop(h)
    s = x + y 
    total += s 
    push(h, s)
print(total)