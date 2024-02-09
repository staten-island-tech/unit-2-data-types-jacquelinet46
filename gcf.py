def factors(x,y):
    for i in range(1,int(x)):
        factor1= int(x)/int(i)
        factor2= int(y)/int(i)
    if int(x)%i==0==int(y)%i:
        print(factor1)
    else:
        print(int(factor2))

factors(input("give number"), input("give another number"))
