n, k = map(int, input().split())
lst = list(map(int, input().split()))
def ghouls(nums, target):
    l = max(nums)
    r = sum(nums)
    while l < r:
        m = (l + r) // 2
        temp = 0
        cnt = 0
        for i in nums:
            if temp + i > m:
                temp = i
                cnt += 1
            else:
                temp += i 
        if cnt + 1 > target:
            l = m + 1
        else:
            r = m 
    return l
print(ghouls(lst, k))