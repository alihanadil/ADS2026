import heapq 
n = int(input())
h = [-i for i in map(int, input().split())]
heapq.heapify(h)
print(' '.join(str(-i) for i in h))