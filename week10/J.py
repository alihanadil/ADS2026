from collections import deque
import sys 
data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
adj = [[] for _ in range(n)]
visited = [False for _ in range(n)]
for i in range(m):
    v, e = int(data[2 + 2*i]), int(data[3 + 2*i])
    adj[v - 1].append(e - 1)
    adj[e - 1].append(v - 1)
cnt = 0
for v in range(n):
    if not visited[v]:
        q = deque([v])
        visited[v] = True
        cnt += 1
        while q:
            node = q.popleft()
            c = len(adj[node])
            for a in adj[node]:
                if not visited[a]:
                    visited[a] = True 
                    q.append(a)
                    if node == v:
                        if c < len(adj[a]) - 1:
                            cnt += 1
                    else:
                        if c - 1 < len(adj[a]) - 1:
                            cnt += 1
print(cnt)