factoriel=1

while True:
    number=int(input("Factoriel Number: "))
    
    if number<0:
        continue
    elif number==0:
        continue
    else:
        for i in range(1,number+1):
            factoriel=factoriel*i
        break
print("{} Factoriel: {}".format(number,factoriel))
    