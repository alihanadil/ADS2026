def merge(lst, l, m, r):
    n1 = m - l + 1
    n2 = r - m 
    lst1 = lst[l : n1 + l]
    lst2 = lst[m + 1 : m + n2 + 1]
    i, j, k = 0, 0, l 
    while i < n1 and j < n2:
        if lst1[i][0] <= lst2[j][0]:
            lst[k] = lst1[i]
            i += 1
        else:
            lst[k] = lst2[j]
            j += 1
        k += 1
    while i < n1:
        lst[k] = lst1[i]
        k += 1
        i += 1
    while j < n2:
        lst[k] = lst2[j]
        k += 1
        j += 1
def ms(lst):
    n = len(lst)
    size = 1 
    while size <= n - 1:
        ls = 0 
        while ls < n - 1:
            m = min(ls + size - 1, n - 1)
            re = min(ls + 2*size - 1, n - 1)
            if m < re:
                merge(lst, ls, m, re)
            ls += 2*size 
        size *= 2
n = int(input())
lst = []
for i in range(n):
    name, grade = input().split()
    lst.append((grade, name))
ms(lst)
for i in lst:
    print(i[1], i[0])