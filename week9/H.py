def build_lps(p, lim, lp):
    lps = [0]*lp
    k = 0
    ans = 0
    for i in range(1, 2*lim):
        while k > 0 and p[k] != p[i]:
            k = lps[k - 1]
        if p[i] == p[k]:
            k += 1
        lps[i] = k 
        if i % 2 != 0:
            L = (i + 1) // 2
            d = 2*L - lps[i]
            if L % d == 0:
                ans += 1
    return ans
t = input()
n = len(t)
lim = (n-1) // 2
lps = build_lps(t, lim, n)
print(lps)