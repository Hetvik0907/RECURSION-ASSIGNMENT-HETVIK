def count(n):
    if n==0:
        return 0
    if n%10==0:
        return 1+count(n//10)
    return count(n//10)
    
print(count(10020))