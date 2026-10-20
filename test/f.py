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
for _ in range(n):
    a = input().split()
    last, first = a[0], a[1]
    total = 0 
    credits = 0
    length = int(a[2])
    for i in range(length):
        g = grades[a[3 + 2*i]]
        c = int(a[4 + 2*i])
        total += g*c 
        credits += c 
    total /= credits
    h.append((total, last, first))
hs(h)
for s in h:
    total, last, first = s 
    print(' '.join((last, first, f"{total:.3f}")))