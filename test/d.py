n = int(input())
opps = list(map(int, input().split()))
opps.sort()
sums = [0]
for o in opps:
    sums.append(sums[-1] + o)
def upper(lst, target):
    l = 0
    r = len(lst) - 1
    ans = - 1
    while l <= r:
        m = (l + r) // 2
        if lst[m] <= target:
            ans = m 
            l = m + 1 
        else:
            r = m - 1
    return ans 
wons = {0: 0}
for i in range(1, 1000):
    wons[i] = upper(opps, i)
rounds = int(input())
for i in range(rounds):
    p = int(input())
    won = wons[p] + 1
    s = sums[won]
    print(won, s)