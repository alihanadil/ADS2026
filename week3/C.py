n, m = map(int, input().split())
code = []
for i in map(int, input().split()):
    if code:
        code.append(i + code[-1])
    else:
        code.append(i)
# print(code)
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
for i in range(m):
    t = int(input())
    print(lower(code, t) + 1)