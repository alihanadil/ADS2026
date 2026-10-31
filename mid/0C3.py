import heapq 
n = int(input())
h = []
for i in range(n):
    ops = input().split()
    if ops[0] == "add":
        heapq.heappush(h, -int(ops[1]))
    else:
        print(-heapq.heappop(h))