# rush hour: 7 - 10 and 15 - 19

departure = input("")
hour = int(departure[0:2]) 
minute = int(departure[3:5])
distance = 120

while distance != 0:
    if 7 <= hour < 10 or 15 <= hour < 19:
        minute += 10
        distance -= 5
    else:
        minute += 10
        distance -= 10
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        hour = 0

if hour < 10:
    hour = "0" + str(hour)
if minute < 10:
    minute = "0" + str(minute)
print("{}:{}".format(hour, minute))
