numDays = int(input("How many days?"))

total = 0
temp = []

for i in range(1, numDays+1):
    nextDay = input("Day " + str(i) + "'s high temp:")
    total += int(nextDay)
    temp.append(int(nextDay))

avg = round(total/numDays,2)
print("Average = " + str(avg))

count = 0
for i in temp:
    if i > avg:
        count += 1

print(str(count) + " day(s) are greater than average temperature")