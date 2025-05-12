t = int(input(""))
num = int(input(""))
Dmojistan = input("")
Dmojistan = sorted(list(map(int, Dmojistan.split())))
Pegland = input("")
Pegland = sorted(list(map(int, Pegland.split())))
total = 0

if t == 1:
    for i in range(num):
        if Dmojistan[i] > Pegland[i]:
            total += Dmojistan[i]
        else:
            total += Pegland[i]
elif t == 2:
    Pegland.reverse()
    for i in range(num):
        if Dmojistan[i] > Pegland[i]:
            total += Dmojistan[i]
        else:
            total += Pegland[i]

print(total)
