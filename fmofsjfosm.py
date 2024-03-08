def bank():
    accounts = [[1,2,3], [4,5,6,1], [0,7,4,5,4]]
    y = [sum([int(i) for i in account]) for account in accounts]
    print(y)
bank()
""" m = accounts.length
n = accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 10 """