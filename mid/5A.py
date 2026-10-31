n = int(input())
checks = [True for _ in range(n + 1)]
checks[0] = checks[1] = False 
for i in range(2, n + 1):
    for j in range(i*i, n + 1, i):
        checks[j] = False 
cnt = 0 
for i in range(n + 1):
    if checks[i]:
        cnt += 1
print(cnt)