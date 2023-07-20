x=int(input("ENTER AN NUMBER"))
bin=' '
while x!=0:
    d=x%8
    bin=str(d)+bin
    x=x//8
print(bin)    
