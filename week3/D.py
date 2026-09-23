n = int(input())
opps = list(map(int, input().split()))
opps.sort()
sums = [0]
for o in opps:
    sums.append(sums[-1] + o)
rounds = int(input())
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
wons = {0: 0}
for i in range(1, 1001):
    wons[i] = upper(opps, i)
for i in range(rounds):
    p = int(input())
    won = wons[p] +1
    s = sums[won]
    print(won, s)