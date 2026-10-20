import sys 
data = sys.stdin.read().split()
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
            l = 2*curr + 1
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
        h[i], h[0] = h[0], h[i]
        temp = h[0]
        curr = 0
        while True:
            l = 2*curr + 1
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
sys.stdout.write(' '.join(map(str, res)))