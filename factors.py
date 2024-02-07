def factors(x):
    factor = x
    for i in range(1,int(x)):
        allfactors= int(x)/int(i)
        if allfactors==int(allfactors):
            print(int(allfactors))
factors(input("give number"))
print(1)