def length_of_string(n):
   
    if n == "":
        return 0
    
    else:
        return 1 + length_of_string(n[1:])
    

print(length_of_string("Hello"))    