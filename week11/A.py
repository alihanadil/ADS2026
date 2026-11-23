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
seg = []
for i in range(m):
    l, r, c = map(int, input().split())
    seg.append((c, l, r))
seg.sort()
ans = 0
for s in seg:
    c, l, r = s 
    i = find(l)
    while i < r:
        parent[i] = i + 1
        ans += c
        i = find(parent[i])
print(ans)