def pro_digit(n):
    if n==1:
        return n
    else:
        return n%10 * pro_digit(n//10)
    
print(pro_digit(124))    