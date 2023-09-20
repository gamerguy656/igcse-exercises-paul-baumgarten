man = input("enter someone's name")
day = int(input("enter that person's birth day"))
month = int(input("enter that person's birth month"))
year = int(input("enter that person's birth year"))
print(day,"/",month,"/",year)
man2 = input("enter someone else's name")
day2 = int(input("enter that person's birth day"))
month2 = int(input("enter that person's birth month"))
year2 = int(input("enter that person's birth year"))
if year < year2:
    print(man,"is younger")
if year2 < year:
    print(man2,"is younger")


