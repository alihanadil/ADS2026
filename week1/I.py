n = int(input())
decks = []

for i in range(n):
    decks.append([i for i in range(1, int(input()) + 1)])

for deck in decks:
    aside = []
    lst = [i for i in range(len(deck))]
    shuffles = 1

    while deck:
        cards_left = len(deck)
        effective = shuffles % cards_left
        deck = deck[effective:] + deck[:effective]  
        aside.append(deck[0])
        deck = deck[1:]
        shuffles += 1

    for k, pos in enumerate(aside):
        lst[pos - 1] = k + 1
        
    for i in lst:
        print(i, end=" ")
    print()