sentence = input("type in a sentence")
vowels = ['a','e','i','o','u']
total=0
for i in range(0,len(sentence)):
    if sentence[i] in vowels:
        total = total+1
print(total)

    
    
