""" def palindrome(c):
    x=c[::-1]
    if c == x:
        return True
palindrome(input())

def prime(x):
    for i in range(2,x):
        if x%i != 0:
            return False """
alpha="a"
xtwo="the quick brown fox jumps over the lazy dog"
for i in alpha:
    if i not in xtwo: