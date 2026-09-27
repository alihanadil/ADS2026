def lower(nums, target):
    l, r = 0, len(nums)          # r is exclusive
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l

def upper(nums, target):
    l, r = 0, len(nums)          # r is exclusive
    while l < r:
        m = (l + r) // 2
        if nums[m] <= target:
            l = m + 1
        else:
            r = m
    return l
n, q = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in range(q):
    query = list(map(int, input().split()))
    l1 = lower(lst, query[0]) + 1
    r1 = upper(lst, query[1])
    l2 = lower(lst, query[2]) + 1
    r2 = upper(lst, query[3])
    length1 = r1 - l1 + 1
    length2 = r2 - l2 + 1
    cross = max(0, min(r1, r2) - max(l1, l2) + 1)
    print(length1 + length2 - cross)

from bisect import bisect_left, bisect_right
n, q = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in range(q):
    query = list(map(int, input().split()))
    l1 = bisect_left(lst, query[0]) + 1
    r1 = bisect_right(lst, query[1])
    l2 = bisect_left(lst, query[2]) + 1
    r2 = bisect_right(lst, query[3])
    length1 = r1 - l1 + 1
    length2 = r2 - l2 + 1
    cross = max(0, min(r1, r2) - max(l1, l2) + 1)
    print(length1 + length2 - cross)