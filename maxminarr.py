def max_ele(arr, n): 
    n=len(arr)
  
    if (n == 1): 
        return arr[0]   
    
    return max(arr[n - 1], max_ele(arr, n - 1)) 




def  min_ele(arr, n): 
      
    if (n == 1): 
        return arr[0]
    
    return min(arr[n - 1], min_ele(arr, n - 1)) 

if __name__ == '__main__':
    arr=[22,34,54,12]
    n=len(arr)
    print(max_ele(arr,n))
    print(min_ele(arr,n))