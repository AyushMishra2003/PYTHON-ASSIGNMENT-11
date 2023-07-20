x=int(input("ENTER AN NUMBER"))
bin=''
while x!=0:
    d=x%2
    bin=str(d)+bin
    x=x//2
print(bin)    