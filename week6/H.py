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
chars = input().split()
char = input()
hs(chars)
found = False
for c in chars:
    if c > char:
        print(c)
        found = True 
        break

if not found:
    print(chars[0])