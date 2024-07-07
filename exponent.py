def cal_pow(a,b):
    if b==0:
        return 1
    else:
        return a*cal_pow(a,b-1)
    
print(cal_pow(4,2))    