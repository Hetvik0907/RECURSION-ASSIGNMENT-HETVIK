
def pattern(n,m):
    if(n==1 or m==1):
        return 1
    else:
        return pattern(n,m-1)+pattern(n-1,m)
    
print(pattern(3,3))    