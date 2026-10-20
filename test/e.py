def hs(heap):
    n = len(heap)
    h = heap 
    for i in range(n // 2 - 1, -1, -1):
        temp = h[i]
        curr = i 
        while True:
            l = 2*curr + 1
            r = l + 1
            if l >= n: break 
            if r < n and h[r] < h[l]:
                maxid = r
            else:
                maxid = l 
            if h[maxid] < temp:
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
            l = 2*curr + 1
            r = l + 1
            if l >= i:
                break 
            if r < i and h[r] < h[l]:
                maxid = r 
            else:
                maxid = l 
            if h[maxid] < temp:
                h[curr] = h[maxid]
                curr = maxid 
            else:
                break 
        h[curr] = temp
n, m = map(int, input().split())
h = []
for _ in range(n):
    h.append(list(map(int, input().split())))
new = []
for i in range(m):
    col = [row[i] for row in h]
    hs(col)
    new.append(col)
for i in range(n):
    row = [col[i] for col in new]
    print(' '.join(map(str, row)))