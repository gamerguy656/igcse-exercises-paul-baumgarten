number = int(input("type number"))
fibo2 = 1
fibo = 0
n = 0
while n==0:
    fibo = fibo + fibo2
    fibo2 = fibo + fibo2
    fet = fibo + fibo2
    print (fet)
    if fet > number:
        n=1
    