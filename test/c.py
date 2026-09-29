a, b = map(int, input().split())
code = []
for i in map(int, input().split()):
    if code:
        code.append(code[-1] + i)
    else:
        code.append(i)
def lower(lst, target):
    l, r = 0, len(lst)
    while l < r:
        m = (l + r) // 2
        if lst[m] < target:
            l = m + 1
        else:
            r = m 
    return l 
for i in range(b):
    p = int(input())
    print(lower(code, p) + 1)