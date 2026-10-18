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

n = int(input())
nicks = {}
for i in range(n):
    old, new = input().split()
    if old in nicks:
        nicks[new] = nicks.pop(old)
    else:
        nicks[new] = old 
new = []
for k, v in nicks.items():
    new.append((v, k))
nicks = new
n = len(nicks)
hs(nicks)
print(n)
for i in nicks:
    print(' '.join(i))