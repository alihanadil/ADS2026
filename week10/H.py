from collections import deque
n, m = map(int, input().split())
grid = []
for i in range(n):
    grid += [int(i) for i in input()]

cnt = 0
for v in range(n*m):
    if grid[v] == 1:
        cnt += 1
        grid[v] = 2
        q = deque([v])
        while q:
            node = q.popleft()
            r = node // m
            c = node % m
            adj = []
            if r - 1 >= 0:
                adj.append(node - m)
            if r + 1 < n:
                adj.append(node + m)
            if c - 1 >= 0:
                adj.append(node - 1)
            if c + 1 < m:
                adj.append(node + 1)
            for a in adj:
                if grid[a] == 1:
                    grid[a] = 2
                    q.append(a)
print(cnt)