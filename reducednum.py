def reduced_num(n):
  
    if n == 0:
        return 0
    
    
    if n % 2 == 0:
       
        return 1 + reduced_num(n // 2)
    else:
       
        return 1 + reduced_num(n - 1)
    
print(reduced_num(15))    