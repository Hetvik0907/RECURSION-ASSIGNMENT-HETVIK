def sum_array(arr):
    
    if not arr:
        return 0
    else:
        return arr[0] + sum_array(arr[1:])

print(sum_array([1,2,3,4,5]))