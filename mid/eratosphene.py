checks = [True for i in range(10000)]
checks[0] = checks[1] = False
for i in range(2, len(checks)):
    if checks[i]:
        for j in range(i*i, len(checks), i):
            checks[j] = False
n = int(input())
cnt = 0
for i in range(len(checks)):
    if checks[i]:
        cnt += 1
    if cnt == n:
        print(i)
        break
