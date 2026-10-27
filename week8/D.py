n = int(input())
h = []
pref = [0] + list(map(int, input().split()))
for i in range(n):
    h.append(pref[i + 1] - pref[i])
power = 1
for i in range(n):
    num = h[i]//power + 97
    print(chr(num),end="")
    power *= 2