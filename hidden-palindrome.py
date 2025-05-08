word = input("")
length = 0

for i in range(0, len(word)+1):
    for x in range(0, len(word)+1):
        temp = word[i:x]
        if temp == temp[::-1] and len(temp) > length:
            length = len(temp)
            print(temp)

print(length)
