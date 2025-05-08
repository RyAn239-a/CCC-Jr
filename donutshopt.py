available = int(input(""))
events = int(input(""))

for i in range(events):
    sign = input("")
    donuts = int(input(""))
    if sign == "+":
        available += donuts
    elif sign == "-":
        available -= donuts
print(available)