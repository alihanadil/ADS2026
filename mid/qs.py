def partition(lst, l, r):
    lst[r], lst[(l+r)//2] = lst[(l+r)//2], lst[r]
    j = l - 1
    for i in range(l, r):
        if lst[i] < lst[r]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[r], lst[j+1] = lst[j+1], lst[r]
    return j + 1
def qs(lst):
    n = len(lst)
    stack = [(0, n - 1)]
    while stack:
        l, r = stack.pop()
        if l >= r: continue
        p = partition(lst, l, r)
        stack.append((l, p - 1))
        stack.append((p + 1, r))
a = [3, 1, 4, 1, 5]
qs(a)
print(a)