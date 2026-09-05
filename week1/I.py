n = int(input())
decks = []
for i in range(n):
    decks.append([i for i in range(1, int(input()) + 1)].reverse())
for deck in decks:
    for i in range(len(deck)):
        