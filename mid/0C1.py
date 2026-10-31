n = int(input())
lst = list(map(int, input().split()))
p = lst[-1]
i = 0 
for j in range(1, n - 1):
    if lst[j] < p:
        i += 1
        lst[j], lst[i] = lst[i], lst[j]
lst[i+1], lst[-1] = lst[-1], lst[i+1]
print(*lst)