n, t = map(int, input().split())
lst = list(map(int, input().split()))
# print(lst)
def ghoul(nums, k):
    l = max(nums)
    r = sum(nums)
    while l < r:
        m = (l + r) // 2
        temp  = 0
        cnt = 0
        # print("m: ", m)
        for i in nums:
            if temp + i > m:
                # print("temp: ", temp)
                cnt += 1
                temp = i
            else:
                temp += i
        if cnt + 1 > k:
            l = m + 1
        else:
            r = m
        # print("l, r: ", l, r)
    return l
print(ghoul(lst, t))