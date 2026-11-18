def build_lps(p):
    lps = [0] * len(p)
    k = 0
    for i in range(1, len(p)):
        while k > 0 and p[i] != p[k]:
            k = lps[k - 1]
        if p[k] == p[i]:
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
p, k = input().split()
t = input()
ans = kmp(t, p)
if int(k) <= len(ans):
    print("YES")
else:
    print("NO")