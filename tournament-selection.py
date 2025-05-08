wins = 0
loss = 0

for _ in range(6):
    result = input("")
    if result == "w" or result == "W":
        wins = wins + 1;
    if result == "l" or result == "L":
        loss = loss + 1;

if wins == 5 or wins == 6:
    print(1)
elif wins == 3 or wins == 4:
    print(2)
elif wins == 1 or wins == 2:
    print(3)
else:
    print(-1)
    