def bubble_sort(arr, n):
    
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:

            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    
    
    return bubble_sort(arr, n - 1)

arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
bubble_sort(arr, n)
print(arr)