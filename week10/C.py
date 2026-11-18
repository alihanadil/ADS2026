from collections import deque
def bfs(a, b):
    q = deque()
    q.append(a)
    parent = [-1]*(max(a, b)*2)
    parent[a] = a
    while q:
        node = q.popleft()
        for i in (node*2, node - 1):
            if i >= 1 and i < max(a,b)*2 and parent[i] == -1:
                parent[i] = node
                q.append(i)
    ans = []
    x = b
    while x != a:
        ans.append(x)
        x = parent[x]
    print(len(ans))
    print(*reversed(ans))
a, b = map(int, input().split())
bfs(a, b)