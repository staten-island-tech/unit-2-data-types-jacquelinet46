bill=10

service= (input("how was your service?"))
if service == "bad":
    print(int(bill)*1)
elif service == "okay":
    print(int(bill)*1.15)
elif service == "good":
    print(int(bill)*1.20)
elif service == "great":
    print(int(bill)*1.25)
else:
    print("what does that mean??????")
