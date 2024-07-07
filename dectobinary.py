def dectobin(n):
    if(n==0):
        return 0
    else:
        dectobin(n // 2) 
        return n % 2 
    
print(dectobin(13))    