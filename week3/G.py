n, m = map(int, input().split())
lst = list(map(int, input().split()))

def cut(ropes, k):
    l = 0
    r = max(ropes)
    times = 0
    while times < 100:
        m = (l + r) / 2
        cnt = 0
        for i in ropes:
            cnt += i // m
        if cnt >= k:
            l = m 
        else:
            r = m 
        # print(l, r, m)
        times += 1
    return l 
ans = cut(lst, m)
print(f"{ans:.9f}")