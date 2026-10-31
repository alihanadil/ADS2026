def binary_search(lst, x):
    l = 0 
    r = len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if lst[m] < x:
            l = m + 1
        elif lst[m] > x:
            r = m - 1
        else:
            return "Yes"
    return "No"
n = int(input())
lst = list(map(int, input().split()))
k = int(input())
print(binary_search(lst, k))