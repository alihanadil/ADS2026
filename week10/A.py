from collections import deque
def bfs(grid, m, n):
    q = deque()
    cnt = 0
    for v in range(m*n):
        if grid[v] == 2:
            q.append(v)
    while q:
        crushed = False
        for i in range(len(q)):
            node = q.popleft()
            r = node // n 
            c = node % n
            v = r*n + c
            adj = []
            if r - 1 >= 0:
                adj.append(v - n)
            if r + 1 < m:
                adj.append(v + n)
            if c - 1 >= 0:
                adj.append(v - 1)
            if c + 1 < n:
                adj.append(v + 1)
            for a in adj:
                if grid[a] == 1:
                    crushed = True
                    grid[a] = 2
                    q.append(a)
        if crushed:
            cnt += 1
    return cnt if 1 not in grid else -1
m, n = map(int, input().split())
grid = []
for i in range(m):
    grid += list(map(int, input().split()))
print(bfs(grid, m, n))