from collections import Counter
s = input()
n = int(input())
b = 31 
m = 10**10
h_s = [0] * (len(s) + 1)
ls = len(s)
cache = {}
for i in range(len(s)):
    h_s[i + 1] = (h_s[i]*b + ord(s[i])) % m
for i in range(n):
    l, r = map(int, input().split()) 
    lt = r - l + 1
    bt = pow(b, lt, m)
    if lt not in cache:
        hashes = [(a - c*bt) % m for a,c in zip(h_s[lt :], h_s)]
        cnt = Counter(hashes)
        cache[lt] = cnt 
    w = (h_s[r] - h_s[l-1]*bt) % m 
    print(cache[lt][w])