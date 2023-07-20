sum=0
digit=int(input("ENTER AN NUMBER"))
for x in range(0,digit):
    if digit:
        a=digit%10
        sum+=a
        digit=digit//10
    else:
        break    
print("SUM OF DIGIT IS ",sum)