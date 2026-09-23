k = int(input())
lst = list(map(int, input().split()))

a, b = map(int, input().split())
snake = []

def row(nums, target):
    l = 0
    r = len(nums) 
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            r = m
        else:
            l = m + 1
    return l - 1
def binary(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1

firsts = []
for i in range(a):
    snake.append(list(map(int, input().split())))
    if i % 2 == 0:
        firsts.append(snake[-1][0])
    else:
        firsts.append(snake[-1][-1])

for i in range(k):
    el = lst[i]
    r = row(firsts, el)
    col = binary(snake[r], el) if r % 2 != 0 else row(snake[r], el)
    if col is None or snake[r][col] != el:
        print(-1)
        continue
    print(r, col)
