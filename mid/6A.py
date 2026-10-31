n = int(input())
q = []
for i in range(n):
    ops  = input().split()
    if ops[0] == "push":
        q.append(ops[1])
    else:
        print(q.pop(0))
# if tle
from collections import deque
q = deque()
for i in range(n):
    ops  = input().split()
    if ops[0] == "push":
        q.append(ops[1])
    else:
        print(q.popleft())