a = ['z', 'y', 'x', 'w', 'v', 't', 's', 'r', 'q', 'p', 'n', 'm', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 'c', 'b', 'u', 'o', 'i', 'e', 'a']

n = int(input())
h = []
for i in input():
    h.append(a.index(i))

def heapify(heap, i, n):
    l = 2*i + 1
    r = 2*i + 2
    minid = i
    if l < n and heap[l] < heap[minid]:
        minid = l
    if r < n and heap[r] < heap[minid]:
        minid = r
    if minid != i:
        heap[i], heap[minid] = heap[minid], heap[i]
        heapify(heap, minid, n)

def hs(heap):
    n = len(heap)
    for i in range(n // 2- 1, -1, -1):
        heapify(heap, i, n)
    for i in range(n - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, 0, i)

hs(h)
print(''.join(a[i] for i in h))