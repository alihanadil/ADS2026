n = int(input())
mod = 10**9 + 7 
cnt = 0 
nums = []
for i in range(2*n):
    nums.append(input())
all_nums = set(nums)
for num in nums:
    h = 0
    power = 1
    for i in num:
        h = (h + (ord(i) - 47)*power) % mod 
        power = power * 11 % mod
    if str(h) in all_nums:
        cnt += 1
        print(f'Hash of string "{num}" is {h}')
    if cnt == n:
        break 