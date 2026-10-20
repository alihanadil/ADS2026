import sys, heapq
data = sys.stdin.read().split()
n = int(data[0])
h = list(map(int, data[1 : n + 1]))
heapq.heapify(h)
m = float('inf')
res = []
prev = heapq.heappop(h)
for _ in range(n - 1):
    curr = heapq.heappop(h)
    d = curr - prev
    if d < m:
        m = d
        res = [f"{prev} {curr}"]
    elif d == m:
        res.append(f"{prev} {curr}")
    prev = curr
sys.stdout.write(' '.join(res))