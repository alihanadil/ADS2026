def merge(lst, lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    i, j, k = 0, 0, 0 
    while i < n1 and j < n2:
        if lst1[i] <= lst2[j]:
            lst[k] = lst1[i]
            i += 1
        else:
            lst[k] = lst2[j]
            j += 1
        k += 1
    while i < n1:
        lst[k] = lst1[i]
        i += 1
        k += 1
    while j < n2:
        lst[k] = lst2[j]
        j += 1
        k += 1
n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))
merged = [i for i in range(n + m)]
merge(merged, l1, l2)
print(*merged)