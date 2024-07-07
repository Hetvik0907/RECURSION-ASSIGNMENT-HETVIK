def sum_array(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum_array(arr[1:])
    
def mean_array(arr):
  
    total_sum = sum_array(arr)
    mean = total_sum / len(arr)
    return mean    


print(mean_array([1,2,3,4,5]))