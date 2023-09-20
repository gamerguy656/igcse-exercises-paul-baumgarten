phone = input("Phone number")
print(phone.isnumeric())
if len(phone) == 8:
    if phone.isnumeric():
        print("that is a phone number")
elif len(phone) == 13:
    if phone.startswith("852 "):
        if phone[4:8].isnumeric() and phone[9:13].isnumeric:
            print("thats a phone number")