# heapq
import heapq
n, m = map(int, input().split())
sums = []
heapq.heapify(sums)
s = 0
for i in range(n):
    com = input().split()
    if com[0] == "insert":
        if len(sums) < m:
            s += int(com[1])
            heapq.heappush(sums, int(com[1]))
        elif sums[0] < int(com[1]):
            s -= heapq.heappop(sums)
            heapq.heappush(sums, int(com[1]))
            s += int(com[1])
    else:
        print(s)

# non heapq
n, m = map(int, input().split())
sums = []
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
s = 0
for i in range(n):
    com = input().split()
    if com[0] == "insert":
        if len(sums) < m:
            s += int(com[1])
            push(sums, int(com[1]))
        elif sums[0] < int(com[1]):
            s -= pop(sums)
            push(sums, int(com[1]))
            s += int(com[1])
    else:
        print(s)