digit=int(input("ENTER AN NUMBER"))
sum=1
for x in range(0,digit):
    digit=digit//10
    if digit:
        sum+=1
    else:
        break
print(sum)                