from collections import deque
def bfs(grid, n, s, e):
    q = deque()
    cnt = 0
    pos = []
    for i in range(n):
        new = []
        for j in range(n):
            if grid[i][j] == 1:
                new.append(j)
        pos.append(new)
    q.append(s)
    dist = {s: 0}
    visited = [False for _ in range(n)]
    visited[s] = True
    cnt = 0
    while q:
        node = q.popleft()
        for i in pos[node]:
            if not visited[i]:
                q.append(i)
                dist[i] = 1 + dist.get(node, 0)
                visited[i] = True
    return dist.get(e, -1)
n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
s,e = map(int, input().split())
print(bfs(grid, n, s - 1, e - 1))