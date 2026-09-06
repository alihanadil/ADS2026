n = int(input())
queue = list(map(int, input().split()))
pos = []
stack = []

for i in queue:
    age = i

    while stack:
        if stack[-1] >= age:
            stack.pop()
        else:
            break

    if stack:
        pos.append(stack[-1])
    else:
        pos.append(-1)
        
    stack.append(i)

for i in pos:
    print(i, end=" ")

