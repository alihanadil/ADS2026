from collections import deque
def bfs(adj, s, f, n):
    visited = [False for i in range(n)]
    visited[s - 1] = True 
    q = deque([s - 1])
    while q:
        node = q.popleft()
        for v in adj[node]:
            if not visited[v]:
                visited[v] = True 
                if v == f - 1:
                    print("YES")
                    return 
                q.append(v)
    print("NO")
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for i in range(m):
    v,e = map(int, input().split())
    adj[v - 1].append(e - 1)
    adj[e - 1].append(v - 1)
s, f = map(int, input().split())
bfs(adj, s, f, n)