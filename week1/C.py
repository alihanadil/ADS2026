n = int(input())

def is_prime(n):
    if n == 1:
        return "NO"
    div = 2
    while div <= n**0.5:
        if n % div == 0:
            return "NO"
        div += 1
    return "YES"

print(is_prime(n))