number = int(input("number"))
mans = []
for x in range(0, number):
    a = int(input("another number"))
    mans.append(a)
print(mans)

total = 0
for n in range (0, len(mans)):
    total = total + mans[n]
print(total)
average = total / number
print("the average would be  ",average)