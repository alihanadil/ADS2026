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
                q.append(v)
    return len(top) == n

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
indeg = [0 for _ in range(n)]
pred = [[] for _ in range(n)]
for i in range(m):
    v, e = map(int, input().split())
    adj[v - 1].append(e - 1)
    indeg[e - 1] += 1
    pred[e - 1].append(v - 1)

c = indeg[:]
if is_acyc(adj, c, n):
    print("YES")
else:
    back = lambda x: next(u for u in pred[x] if c[u] > 0)
    v = next(i for i in range(n) if c[i] > 0)
    for _ in range(n):
        v = back(v)
    cycle = [v]
    x = back(v)
    while x != v:
        cycle.append(x)
        x = back(x)
    for i in cycle:
        tmp = indeg[:]
        tmp[i] -= 1
        if is_acyc(adj, tmp, n):
            print("YES")
            break
    else:
        print("NO")