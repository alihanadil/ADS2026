from collections import deque
INF = 10**9
def bfs(adj, d, s):         
    d[s] = 0
    q = deque([s])
    while q:
        node = q.popleft()
        for u in adj[node]:
            if d[u] > d[node] + 1:
                d[u] = d[node] + 1
                q.append(u)
n, m, q = map(int, input().split())
adj = [[] for _ in range(n)]
d = [INF] * n                    
for i in range(m):
    v, e = map(int, input().split())
    adj[v - 1].append(e - 1)
    adj[e - 1].append(v - 1)
for i in range(q):
    a, b = map(int, input().split())
    if a == 1:
        bfs(adj, d, b - 1)
    else:
        print(d[b - 1] if d[b - 1] != INF else -1)