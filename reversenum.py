def reverse(n,r):
    if n<1:
        return r

    else:
       

        return reverse(n//10, r*10 + n%10)

print(reverse(321,0))        