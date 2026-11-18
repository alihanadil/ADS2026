def build_lps(p):
    lps = [0] * len(p)
    k = 0
    for i in range(1, len(p)):
        while k > 0 and p[k] != p[i]:
            k = lps[k - 1]
        if p[k] == p[i]:
            k += 1
        lps[i] = k 
    return lps 
def kmp(t, p, k, lps, lp):
    for c in t:
        while k[-1] > 0 and c != p[k[-1]]:
            k[-1] = lps[k[-1] - 1]
        if c == p[k[-1]]:
            k[-1] += 1
        if k[-1] == lp:
            return True 
    return False
t = input()
p = input()
lps = build_lps(p)
lp = len(p)
k = [0]
res = None 
needed = (len(t) - 1) + lp 
limit = (needed + len(t) + 1) // len(t)
n = 1
while True:
    res = kmp(t, p, k, lps, lp)
    if res:
        print(n)
        break
    elif n == limit:
        print(-1)
        break 
    n += 1