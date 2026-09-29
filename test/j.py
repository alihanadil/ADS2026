n, k = map(int, input().split())
lst = []
l, r = 0, 0
for i in range(n):
    lst.append(list(map(int, input().split())))
    r = max(r, lst[-1][2], lst[-1][3])
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