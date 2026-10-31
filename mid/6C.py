import heapq 
n = int(input())
h = []
for i in map(int, input().split()):
    heapq.heappush(h, -i)
while len(h) > 1:
    x = heapq.heappop(h)
    y = heapq.heappop(h)
    s = abs(y - x)
    if s != 0:
        heapq.heappush(h, -s)
print(-h[0] if h else 0)