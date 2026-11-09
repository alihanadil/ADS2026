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
def kmp(t, p, lps, k, lp):
    res = []
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
lp = len(p)
lps = build_lps(p)
n = 1
k = [0]
res = None
needed = (len(t) - 1) + lp 
limit = (needed  + len(t) - 1)//len(t)
while True:
    res = kmp(t, p, lps, k, lp)
    if res == True:
        print(n)
        break
    elif n == limit:
        print(-1)
        break
    n += 1 