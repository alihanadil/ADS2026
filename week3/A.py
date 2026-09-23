a = int(input())
lst = list(map(int, input().split()))
b = int(input())
exist = False
l = 0
r = len(lst) - 1
while l <= r:
    m = (l + r) // 2
    # print(lst[m], " ", b)
    if lst[m] == b:
        exist = True
        break
    elif lst[m] > b:
        r = m - 1
    else:
        l = m + 1

print("Yes" if exist else "No")