from collections import Counter
s = input()
n = int(input())
b = 31
mod = 10**10
h_s = [0] * (len(s) + 1)
ls = len(s)
cache = {}
for i in range(ls):
    h_s[i+1] = (h_s[i]*b + ord(s[i])) % mod
for i in range(n):
    l, r = map(int, input().split())
    lt = r - l + 1
    bt = pow(b, lt, mod)
    if lt not in cache:
        hashes = [(a - c*bt) % mod for (a, c) in zip(h_s[lt: ], h_s)]
        cnt = Counter(hashes)
        cache[lt] = cnt 
    w = (h_s[r] - h_s[l - 1]*bt) % mod 
    print(cache[lt][w])