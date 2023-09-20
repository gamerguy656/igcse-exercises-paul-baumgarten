phonenumber = int(input("type a phone number"))
result = phonenumber.startswith("852")
n = len(phonenumber)

if result:
    if n == 13:
        print("hong kong phone number")
else:
    print("not hong kong phone number")
