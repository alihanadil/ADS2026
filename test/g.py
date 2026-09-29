n, k = map(int, input().split())
lst = list(map(int, input().split()))

def ropes(nums, target):
    l = 0
    r = max(nums)
    times = 0
    while times < 100:
        m = (l + r) / 2
        cnt = 0
        for i in nums:
            cnt += i // m 
        if cnt >= target:
            l = m 
        else:
            r = m 
        times += 1
    return l 
ans = ropes(lst, k)
print(f"{ans:.9f}")