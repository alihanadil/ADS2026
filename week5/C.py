n, k = map(int, input().split())
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
    push(h, -i)
cnt = 0
total = 0
while cnt < k:
    num = pop(h)
    total += -num 
    push(h, num + 1)
    cnt += 1
print(total)