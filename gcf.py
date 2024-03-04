x=int(input("give number"))
y=int(input("give another number"))
gcf=[]
def gcfcalc():
    for i in range(1,x):
        if x%i == 0 and y%i == 0:
            gcf.append(i)
gcfcalc()
print(gcf)
#factors=[]
#factor.append(x)2
