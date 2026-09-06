boris = list(map(int, input().split()))
nursik = list(map(int, input().split()))
moves = 0

while boris and nursik:
    b = boris[0]
    n = nursik[0]
    if (b > n and (n != 0 or b != 9)) or (b == 0 and n == 9):
        # print("Boris: ", b, "Nurski: ", n)
        boris = boris[1: ]
        boris.append(b)
        nursik = nursik[1: ]
        boris.append(n)
    elif (n > b and (b != 0 or n != 9)) or (n == 0 and b == 9):
        # print("Boris: ", b, "Nurski: ", n)
        boris = boris[1: ]
        nursik.append(b)
        nursik = nursik[1: ]
        nursik.append(n)
    moves += 1
print(f"Boris {moves}" if not nursik else f"Nursik {moves}")