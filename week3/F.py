n, h = map(int, input().split())
lst = list(map(int, input().split()))

def good(bags, h):
    l = 1
    r = max(bags) 
    while l < r:
        m = (l + r) // 2
        cnt = 0
        for i in bags:
            cnt += i // m if i % m == 0 else i // m + 1
        if cnt <= h:
            r = m 
        else:
            l = m + 1
    return l
print(good(lst, h))