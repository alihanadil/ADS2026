import heapq

def prim(adj, n):
    pq = []
    visited = [False for _ in range(n)]
    res = 0
    heapq.heappush(pq, (0, 0))
    while pq:
        w, v = heapq.heappop(pq)
        if visited[v]:
            continue
        res += w
        visited[v] = True
        for a in adj[v]:
            if not visited[a[0]]:
                heapq.heappush(pq, (a[1], a[0]))
    return res
n = int(input())
adj = [[] for i in range(n)]
grid = []
for i in range(n):
    grid += list(map(int, input().split()))
j = 0
for i in range(len(grid)):
    c = i % n 
    r = i // n 
    if c != r:
        adj[c].append((r, grid[i]))
print(prim(adj, n))