t = int(input())
list_f = []
for i in range(t):
    n = int(input())
    lst = input().split()
    new_lst = []
    count = dict()
    queue = []
    for j in range(n):
        char = lst[j]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
        if char not in queue:
            queue.append(char)
        while queue and count[queue[0]] > 1:
            queue = queue[1 : ]
        if not queue:
            new_lst.append(-1)
        else:
            new_lst.append(queue[0])
        
            
    list_f.append(new_lst)

for i in list_f:
    for j in i:
        print(j, end=" ")
    print()