n = int(input())
factors = []
checks = [True for i in range(int(n**0.5) + 1)] if n > 9 else [True for i in range(n)]
checks[0] = checks[1] = False
for i in range(2, len(checks)):
    if checks[i]:
        for j in range(i*i, len(checks), i):
            checks[j] = False
                
# for i in range(len(checks)):
#     if checks[i]:
#         print(i, end=" ")

for i in range(2, len(checks)):
    if checks[i]:
        while n % i == 0:
            factors.append(i)
            n //= i
if n > 1:
    factors.append(n)
for i in factors:
    print(i, end=" ")