n = int(input())
def sqrt(n):
    l = 1 
    r = n 
    while l <= r:
        m = (l+r) // 2
        if m*m <= n:
            l = m + 1
        else:
            r = m - 1
    return r 
for i in map(int, input().split()):
    print(sqrt(i))
