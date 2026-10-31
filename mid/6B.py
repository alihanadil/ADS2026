def lower(lst, x):
    l = 0 
    r = len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if lst[m] >= x:
            r = m - 1 
        else:
            l = m + 1
    return l
n = int(input())
lst = list(map(int, input().split()))
m = int(input())
for i in map(int, input().split()):
    low = lower(lst, i)
    print(low + 1 if low < n else -1)