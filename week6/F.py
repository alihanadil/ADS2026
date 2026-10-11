def heapify(heap, i, n):
    temp = heap[i]
    while True:
        l = 2*i + 1
        r = l + 1
        if l >= n:
            break 
        if r < n and heap[r] > heap[l]:
            maxid = r 
        else:
            maxid = l 
        if heap[maxid] > temp:
            heap[i] = heap[maxid]
            i = maxid 
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
grades ={
    "A+": 4.00,
    "A": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "C+": 2.50,
    "C": 2.00,
    "D+": 1.50,
    "D": 1.00,
    "F": 0
}
n = int(input())
h = []
for i in range(n):
    a = input().split()
    last, first = a[0], a[1]
    credits = 0
    total = 0
    length = int(a[2])
    for j in range(length):
        g = grades[a[3 + 2 * j]]
        c = int(a[4 + 2 * j])
        total += g*c
        credits += c
    total = total/credits
    h.append((total, last, first))
hs(h)
for s in h:
    total, last, first = s 
    print(' '.join((last, first, f"{total:.3f}")))