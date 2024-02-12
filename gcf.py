def gcfcalc(x,y):
    while y!=0:
        z=y
        y=int(x)%int(y)
        x=z
    return x

x=int(input("give number"))
y=int(input("give another number"))

gcf=gcfcalc(x,y)
print(gcf)
#factors=[]
#factor.append(x)2
