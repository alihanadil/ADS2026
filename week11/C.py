n, m = map(int, input().split())
x, y = map(int, input().split())
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
road = []
for i in range(m):
    s, l, r, c = input().split()
    if s == "small":
        cost = y * int(c)
    elif s == "big":
        cost = x * int(c) 
    else:
        cost = x * int(c)
        road.append((cost, int(l), int(r)))
        cost = y * int(c) 
    road.append((cost, int(l), int(r)))
road.sort()
ans = 0
for a in road:
    c, l, r = a 
    if union(l, r):
        ans += c
print(ans)