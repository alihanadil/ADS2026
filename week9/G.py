def build_lps(p):
    lps = [0]*len(p)
    k = 0
    for i in range(1, len(p)):
        while k > 0 and p[k] != p[i]:
            k = lps[k - 1]
        if p[i] == p[k]:
            k += 1
        lps[i] = k 
    return lps
t = input()
lps = build_lps(t)
print(len(t) - lps[-1])