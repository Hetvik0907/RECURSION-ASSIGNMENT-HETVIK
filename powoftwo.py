def is_power(n):
    n = n/2
    if n == 2:
        return True
    elif n > 2:
        is_power(n)
    else:
        return False


print(is_power(32))