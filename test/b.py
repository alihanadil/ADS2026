n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))
i, j = 0, 0 
while i < n and j < m:
    if lst1[i] <= lst2[j]:
        print(lst1[i], end=" ")
        i += 1
    else:
        print(lst2[j], end=" ")
        j += 1
while i < n:
    print(lst1[i], end=" ")
    i += 1
while j < m:
    print(lst2[j], end=" ")
    j += 1