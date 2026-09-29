a = int(input())
lst = list(map(int ,input().split()))
b = int(input())
l = 0
r = len(lst)
exist = False
while l < r:
    m = (l + r) // 2
    if lst[m] == b:
        exist = True
        break
    elif lst[m] < b:
        l = m + 1
    else:
        r = m 
print("YES" if exist else "NO")