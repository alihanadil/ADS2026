def merge(lst, l, m, r):
    n1 = m - l + 1
    n2 = r - m 
    lst1 = lst[l : l + n1]
    lst2 = lst[m + 1 : m + n2 + 1]
    i, j, k = 0, 0, l 
    while i < n1 and j < n2:
        si = sum(lst1[i])
        sj = sum(lst2[j])
        if si > sj:
            lst[k] = lst1[i]
            i += 1
        elif si == sj:
            if lst1[i] < lst2[j]:
                lst[k] = lst1[i]
                i += 1
            else:
                lst[k] = lst2[j]
                j += 1
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
def ms(lst):
    n = len(lst) - 1
    size = 1
    while size <= n:
        ls = 0 
        while ls < n:
            m = min(ls + size - 1, n)
            re = min(ls + 2*size - 1, n)
            merge(lst, ls, m, re)
            ls += 2*size 
        size = 2*size 
n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ms(a)
for i in a:
    print(*i)