# Predic the output

# Optimized version
def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        didswap = 0
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didswap = 1
        if didswap == 0:
            break     
    return arr
    
numbers = [2, 4, 6, 8, 12]
sorted_arr = bubble_sort(numbers)   
print(sorted_arr)            

