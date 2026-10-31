n = int(input())
def is_prime(n):
    if n == 1:
        return "NO"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "NO"
    return "YES"
print(is_prime(n))