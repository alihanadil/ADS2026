a, n, m = map(int, input().split())

def bin_exp(a, n):
    if n == 0:
        return 1 % m
    if n % 2 == 0:
        return (bin_exp(a, n // 2))**2 % m
    return a * bin_exp(a, n - 1) % m

print(bin_exp(a, n))
