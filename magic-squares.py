magic = 0
square = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
        row = input("")
        arr = [int(y) for y in row.split()]
        for x in range(4):
                square[i][x] = arr[x]

sum = square[0][0] + square[0][1] + square[0][2] + square[0][3]

for i in range(4):
        sumnext = 0
        for x in range(4):
              sumnext = sumnext + square[i][x]
        if sumnext != sum:
                print("not magic")
                quit()
        
for i in range(4):
        sumnext = 0
        for x in range(4):
                sumnext = sumnext + square[x][i]
        if sumnext != sum:
                print("not magic")
                quit()

print("magic")

"""
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
"""