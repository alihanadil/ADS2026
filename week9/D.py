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
city = input().lower()
n = int(input())
res = []
best = 0
for i in range(n):
    new = input().lower()
    ans = build_lps(new + '#' + city)
    if best < ans[-1] :
        best = ans[-1]
        res = [new.capitalize()]
    elif best == ans[-1] and ans[-1] != 0:
        res.append(new.capitalize())
print(len(res))
for i in res:
    print(i)