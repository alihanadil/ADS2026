n = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())

snake = []

def row(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            r = m 
        else:
            l = m + 1
    return l - 1
def col(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m 
        else:
            l = m + 1
    return - 1
firsts = []
for i in range(a):
    snake.append(list(map(int, input().split())))
    if i % 2 == 0:
        firsts.append(snake[-1][0])
    else:
        firsts.append(snake[-1][-1])
for i in lst:
    r = row(firsts, i)
    c = col(snake[r], i) if r % 2 != 0 else row(snake[r], i)
    if c == -1 or snake[r][c] != i:
        print(-1)
        continue
    print(r, c)