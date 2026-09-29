def upper(lst, target):
    l,r  = 0, len(lst)
    while l < r:
        m = (l + r) // 2
        if lst[m] <= target:
            l = m + 1
        else:
            r = m
    return l 
def lower(lst, target):
    l, r = 0, len(lst)
    while l < r:
        m = (l + r) // 2
        if lst[m] < target:
            l = m + 1
        else:
            r = m 
    return l 
a, b = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for i in range(b):
    query = list(map(int, input().split()))
    l1 = lower(nums, query[0]) + 1
    r1 = upper(nums, query[1])
    l2 = lower(nums, query[2]) + 1
    r2 = upper(nums, query[3])
    length1 = r1 - l1 + 1
    length2 = r2 - l2 + 1
    cross = max(0, min(r1, r2) - max(l1, l2) + 1)
    print(length1 + length2 - cross)