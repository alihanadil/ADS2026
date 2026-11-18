def build_lps(p):
    lps = [0] * len(p)
    k = 0 
    for i in range(1, len(p)):
        while k > 0 and p[i] != p[k]:
            k = lps[k - 1]
        if p[i] == p[k]:
            k += 1
        lps[i] = k 
    return lps 
def kmp(t, p):
    lps = build_lps(p)
    k = 0 
    res = []
    for i, c in enumerate(t):
        while k > 0 and c != p[k]:
            k = lps[k - 1]
        if c == p[k]:
            k += 1
        if k == len(p):
            res.append(i - k + 1)
            k = lps[k - 1]
    return res 
t = input()
p = input()
ans = kmp(p * 2, t)
print(ans[0] if ans else - 1)