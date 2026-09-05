n = int(input())
checks = [True for i in range(8000)]
checks[0] = checks[1] = False
for i in range(2, len(checks)):
    # print("i:", i)
    if checks[i]:
        for j in range(i + 1, len(checks)):
            if j % i == 0:
                # print("i:", i, "j:", j)
                checks[j] = False
i = 0
for j in range(len(checks)):
    if i == n:
        print(j - 1)
        break
    if checks[j]:
        i += 1