n, m = map(int, input().split())
code = []
for i in map(int, input().split()):
    if code:
        code.append(i + code[-1])
    else:
        code.append(i)
# print(code)
def lower(nums, target):
    l, r = 0, len(nums)          # r is exclusive
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l

for i in range(m):
    t = int(input())
    print(lower(code, t) + 1)