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
n = int(input())
for i in range(n):
    p, k = input().split()
    lps = build_lps(p)
    print(len(p) + (len(p) - lps[-1])*(int(k) - 1))