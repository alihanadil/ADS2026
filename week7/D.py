def merge(lst, l, m, r, cnt):
    n1 = m - l + 1
    n2 = r - m 
    lst1 = lst[l : l + n1]
    lst2 = lst[m + 1: m + n2 + 1]

    i,j = 0, 0 
    k = l 

    while i < n1 and j < n2:
        if lst1[i] <= lst2[j]:
            lst[k] = lst1[i]
            i += 1
        else:
            cnt[-1] += n1 - i
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
    
def ms(lst, cnt):
    n = len(lst) - 1
    size = 1
    while size <= n:
        ls = 0 
        while ls < n:
            m = min(ls + size - 1, n)
            re = min(ls + 2*size - 1, n)
            merge(lst, ls, m, re, cnt)
            ls += 2*size 
        size = 2*size
n = int(input())
lst = list(map(int, input().split()))
c = [0]
ms(lst, c)
# print(lst)
print(c[0])