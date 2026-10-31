def binary_exp(a, n, m):
    if n == 0:
        return 1 % m 
    if n % 2 == 0:
        return binary_exp(a, n // 2, m)**2 % m 
    return a*binary_exp(a, n - 1, m) % m
a, n, m = map(int, input().split())
print(binary_exp(a, n, m))