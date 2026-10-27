from collections import Counter
n = int(input())
b = 31
m = 10**9 + 7 
while n != 0:
    tar = []
    cache = {}
    for i in range(n):
        tar.append(input())
    s = input()
    h_s = [0] * (len(s) + 1)
    counts = []
    for i in range(len(s)):
        h_s[i + 1] = (h_s[i]*b + ord(s[i])) % m
    for t in tar:
        lt = len(t)
        h = 0 
        for c in t:
            h = (h*b + ord(c)) % m 
        if lt not in cache:
            bt = pow(b, lt, m)
            hashes = [(a-c*bt) % m for (a, c) in zip(h_s[lt: ], h_s)]
            cnt = Counter(hashes)
            cache[lt] = cnt
        counts.append((cache[lt][h], t))
    maximum = max(counts)[0]
    print(maximum)
    for cnt, pat in counts:
        if cnt == maximum:
            print(pat)
    n = int(input())