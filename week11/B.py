n = input()
isles = list(map(int, input().split()))
a = min(isles)
total = -2*a
for i in isles:
    total += a + i
print(total)