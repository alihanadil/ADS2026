def partition(arr, l, r):
    arr[r], arr[(l + r) // 2] = arr[(l + r) // 2], arr[r]
    j = l - 1
    for i in range(l, r):
        if arr[i] < arr[r]:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[r], arr[j + 1] = arr[j + 1], arr[r]
    return j + 1
def qs(arr):
    n = len(arr)
    stack = [(0, n - 1)]
    while stack:
        l, r = stack.pop()
        if l >= r: continue
        p = partition(arr, l, r)
        stack.append((l, p - 1))
        stack.append((p + 1, r))

n = int(input())
nicks = {}
for i in range(n):
    old, new = input().split()
    if old in nicks:
        nicks[new] = nicks.pop(old)
    else:
        nicks[new] = old 
new = []
for k, v in nicks.items():
    new.append((v, k))
nicks = new
n = len(nicks)
qs(nicks)
print(n)
for i in nicks:
    print(' '.join(i))