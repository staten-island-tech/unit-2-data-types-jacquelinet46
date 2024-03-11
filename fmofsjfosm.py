accounts = [['1','2','3'], ['4','5','6','1']]

def bank(accounts):
    int_accs = [[int(x) for x in i] for i in accounts]
    largest = 0
    for money in int_accs:
        x = sum(money)
        if x > largest:
            largest = x
    print(largest)
"""     m = accounts.length 
    y = [sum([int(i) for i in account]) for account in accounts]
    n = accounts[3].length
    1 <= m, n <= 50
    1 <= accounts[3][4] <= 10    
    print(y)
    return wrong answer """
#notes
bank(accounts)
