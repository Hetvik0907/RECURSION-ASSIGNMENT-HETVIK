def printNos(n):
    if n > 0:
        print(n, end=' ')
        printNos(n - 1)
        



n = 10
printNos(n)