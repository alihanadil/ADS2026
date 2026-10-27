s = input()
n = len(s)
b = 31
m = 10**10
h = [0] * (n + 1)
pw = [1] * (n + 1)
for i in range(1, n + 1):
    pw[i] = pw[i - 1]*b % m
total = 0
for i in range(n):
    h[i + 1] = (h[i]*b + ord(s[i])) % m
for L in range(1, n + 1):
    seen = set()
    for l in range(0, n - L + 1):
        w = (h[L + l] - h[l]*pw[L]) % m
        seen.add(w)
    total += len(seen)
print(total)