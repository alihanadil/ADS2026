import math 
a, b = map(int, input().split())
gcd = math.gcd(a, b)
lcm = math.lcm(a, b)
print(gcd, lcm)
def mygcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def mylcm(a, b):
    g = mygcd(a, b)
    return abs(a*b)//g
print(mygcd(a, b), mylcm(a, b))
