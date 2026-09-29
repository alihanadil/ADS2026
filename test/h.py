n, k = map(int, input().split())
lst = list(map(int, input().split()))
sums = [0]
for i in lst:
    sums.append(sums[-1] + i)
lens = []
def sub(nums, start, target):
    l = start 
    r = len(nums)
    exist = False 
    while l < r:
        m = (l + r) // 2
        s = nums[m] - nums[start]
        if s >= target:
            r = m 
            exist = True 
        else:
            l = m + 1
    return r - start if exist else len(nums)
for i in range(len(lst)):
    lens.append(sub(sums, i, k))
print(min(lens) if lens else n)