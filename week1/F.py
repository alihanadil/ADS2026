a = input()
b = input()
a1, b1 = [], []

for i in range(len(a)):
    if a[i] == "#" and a1:
        a1.pop()
    elif a[i] != "#":
        a1.append(a[i])

for i in range(len(b)):
    if b[i] == "#" and b1:
        b1.pop()
    elif b[i] != "#":
        b1.append(b[i])

print("Yes" if a1 == b1 else "No")