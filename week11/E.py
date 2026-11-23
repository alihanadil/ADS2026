n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
def find(x):
    lead = x 
    while parent[lead] != lead:
        lead = parent[lead]
    while lead != parent[x]:
        nxt = parent[x]
        parent[x] = lead
        x = nxt 
    return lead
def union(x, y):
    rootx = find(x)
    rooty = find(y)
    if rootx != rooty:
        parent[rootx] = rooty
        return True
    return False
adj = [[] for _ in range(n)]
visited = [False for _ in range(n)]
for i in range(m):
    v, e = map(int, input().split())
    adj[v - 1].append(e - 1)
    adj[e - 1].append(v - 1)
res = []
cnt = 0
for v in range(n, 0, -1):
    res.append(cnt)
    cnt += 1
    visited[v - 1] = True
    for u in adj[v - 1]:
        if visited[u] and union(v - 1, u):
            cnt -=1 
for i in range(n - 1, -1, -1):
    print(res[i])