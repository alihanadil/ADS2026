n = int(input())
h = list(map(int, input().split()))
def sift(h):
    n = len(h)
    for i in range(n // 2 ):
        l = 2*i + 1
        r = l + 1
        if l >= n: break
        if h[l] < h[i]:
            return "NO"
        if r < n and h[r] < h[i]:
            return "NO"
    return "YES"
print(sift(h))