def product(n):
    if n==0:
        return 0
    else:
        return n%10 + product(n//10)
    
print(product(212))    