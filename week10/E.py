n, q = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
for _ in range(q):
    a, i, j = map(int, input().split())
    if grid[a - 1][i - 1] == grid[a - 1][j - 1] == grid[i - 1][j - 1] == 1:
        print("YES")
    else:
        print("NO")