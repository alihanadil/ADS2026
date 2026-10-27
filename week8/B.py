s1 = input()
s2 = input()
t = input()
b = 31
m = 10**9 + 7
lt = len(t)
bt = pow(b, lt, m)
ht = 0
h1 = [0] * (len(s1) + 1)
h2 = [0] * (len(s2) + 1)
cnt = 0
for i in range(lt):
    ht = (ht*b + ord(t[i])) % m 
for i in range(len(s1)):
    h1[i + 1] = (h1[i]*b + ord(s1[i])) % m
for i in range(len(s2)):
    h2[i + 1] = (h2[i]*b + ord(s2[i])) % m
l = 0 
smallest = min(len(s1), len(s2))
while l + lt <= smallest:
    w1 = (h1[l + lt] - h1[l]*bt) % m 
    w2 = (h2[l + lt] - h2[l]*bt) % m
    if w1 == w2 == ht:
        cnt += 1
    l += 1
print(cnt)