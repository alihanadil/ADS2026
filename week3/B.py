
n, q = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
# print(lst)
def upper(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] == target and (m + 1 == len(nums) or nums[m + 1] != target):
            r = m 
            break
        else:
            l = m + 1
    return r
def lower(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] == target and (m == 0 or nums[m - 1] != target):
            l = m
            break
        else:
            r = m - 1
    return l
for i in range(q):
    query = list(map(int, input().split()))
    l1 = lower(lst, query[0])
    r1 = upper(lst, query[1])
    l2 = lower(lst, query[2])
    r2 = upper(lst, query[3])
    # print(l1, r1, l2, r2)
    length1 = r1 - l1 + 1
    length2 = r2 - l2 + 1
    cross = max(0, min(r1, r2) - max(l1, l2) + 1)
    print(length1 + length2 - cross)
# print(lower(lst, 1), upper(lst, 1), lower(lst, 2), upper(lst, 3))