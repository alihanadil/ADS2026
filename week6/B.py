import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    h1 = list(map(int, data[2:2+n]))
    h2 = list(map(int, data[2+n:2+n+m]))
    res = []

    def hs(heap):
        n = len(heap)
        h = heap  
        
        for i in range(n // 2 - 1, -1, -1):
            temp = h[i]
            curr = i
            while True:
                l = 2 * curr + 1
                r = l + 1
                
                if l >= n: 
                    break
                if r < n and h[r] > h[l]:
                    maxid = r
                else:
                    maxid = l
                    
                if h[maxid] > temp:
                    h[curr] = h[maxid]
                    curr = maxid 
                else:
                    break
            h[curr] = temp

        for i in range(n - 1, 0, -1):
            h[0], h[i] = h[i], h[0]
            
            temp = h[0]
            curr = 0
            while True:
                l = 2 * curr + 1
                r = l + 1
                
                if l >= i: 
                    break
                    
                if r < i and h[r] > h[l]:
                    maxid = r
                else:
                    maxid = l
                    
                if h[maxid] > temp:
                    h[curr] = h[maxid]
                    curr = maxid
                else:
                    break
            h[curr] = temp

    hs(h1)
    hs(h2)

    i, j = 0, 0 
    while i < len(h1) and j < len(h2):
        if h1[i] < h2[j]:
            i += 1
        elif h1[i] > h2[j]:
            j += 1
        else:
            res.append(h1[i])
            i += 1
            j += 1
            
    sys.stdout.write(' '.join(map(str, res)) + '')

solve()

#
n, m = map(int, input().split())
h1 = list(map(int, input().split())) if n != 0 else []
h2 = list(map(int, input().split())) if m != 0 else []
res= []
def heapify(heap, i, n):
    temp = heap[i]
    while True:
        l, r = 2*i + 1, 2*i + 2
        maxid = i
        if l < n and heap[l] > temp:
            maxid = l 
        if r < n and heap[r] > heap[maxid]:
            maxid = r 
        if maxid == i:
            break 
        heap[i] = heap[maxid]
        i = maxid 
    heap[i] = temp
        
def hs(heap):
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(heap, i, n)
    for i in range(n - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, 0, i)
hs(h1)
hs(h2)

i, j = 0, 0 
while i < len(h1) and j < len(h2):
    if h1[i] < h2[j]:
        i += 1
    elif h1[i] > h2[j]:
        j += 1
    else:
        res.append(h1[i])
        i += 1
        j += 1
        
print(' '.join(map(str, res)))