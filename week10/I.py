from collections import deque
def is_acyc(adj, indeg, n):
    q = deque([node for node in range(n) if indeg[node] == 0])
    top = []
    while q:
        node = q.popleft()
        top.append(node)
        for v in adj[node]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.appendleft(v)
    if len(top) == n:
        print("Possible")
        print(' '.join(str(i + 1) for i in top))
    else:
        print("Impossible")
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
indeg = [0 for _ in range(n)]
for i in range(m):
    v,e = map(int, input().split())
    adj[v - 1].append(e - 1)
    indeg[e - 1] += 1 
is_acyc(adj, indeg, n)