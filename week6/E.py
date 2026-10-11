def heapify(heap, i, n):
    temp = heap[i]
    while True:
        l = 2*i + 1
        r = l + 1
        if l >= n:
            break 
        if r < n and heap[r] < heap[l]:
            minid = r 
        else:
            minid = l 
        if heap[minid] < temp:
            heap[i] = heap[minid]
            i = minid 
        else:
            break
    heap[i] = temp
        
def hs(heap):
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(heap, i, n)
    for i in range(n - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, 0, i)
n, m = map(int, input().split())
h = []
new = []
for i in range(n):
    h.append(list(map(int, input().split())))
for i in range(m):
    col = [row[i] for row in h]
    hs(col)
    new.append(col)
for i in range(n):
    res = [col[i] for col in new]
    print(' '.join(map(str, res)))