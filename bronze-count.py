number_of_participants = int(input(""))
scores = []
third = 0
number_of_third = 0
for i in range(number_of_participants):
    scores.append(int(input("")))
scores.sort(reverse = True)

count = 0
for i in range(number_of_participants):
    if i == 0:
        count += 1
    else:
        if scores[i] != scores[i-1]:
            count += 1
    if count == 3:
        third = scores[i]
        number_of_third += 1

print(f"{third} {number_of_third}")

""" 
4
70
62
58
73
"""