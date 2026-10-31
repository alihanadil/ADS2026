import bisect
def binary_search(lst, x):
    l = 0
    r = len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if lst[m] > x:
            r = m - 1
        elif lst[m] < x:
            l = m + 1
        else:
            return "YES"
    return "NO"
def binary_search_lib(lst, x):
    idx = bisect.bisect_left(lst, x)
    if idx >= len(lst) or lst[idx] != x:
        return "NO"
    return "YES" 

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
for i in map(int, input().split()):
    print(binary_search(lst, i), sep=" ")
    print(binary_search_lib(lst, i))