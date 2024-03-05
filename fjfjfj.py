def palindrome(c):
    x=c[::-1]
    print(x)
    if c == x:
        return True

palindrome(input("idk type something"))

"""def prime(x):
    for i in range(2,x):
        if x%i != 0:
            return False """