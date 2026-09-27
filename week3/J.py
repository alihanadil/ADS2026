n, k = map(int, input().split())
lst = []
l = 10000
r = 0
for i in range(n):
    lst.append(list(map(int, input().split())))
    m1 = min(lst[-1])
    m2 = max(lst[-1])
    if m2 > r:
        r =  m2
    if m1 < l:
        l = m1
while l < r:
    m = (l + r) // 2
    cnt = 0
    for i in lst:
        if i[2] <= m and i[3] <= m:
            cnt += 1
    if cnt >= k:
        r = m
    else:
        l = m + 1
print(l)