''' Bubble Sort - It pushes the maximum to the last by adjacent swaps '''

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr                

numbers = [29, 10, 14, 37, 13]
sorted_arr = bubble_sort_asc(numbers)
print(sorted_arr)



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
sorted_arr = bubble_sort_desc(numbers)   
print(sorted_arr)            

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        didSwapped = 0
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwapped = 1
        if didSwapped == 0:
            break        
    return arr              

numbers = [29, 10, 14, 37, 13]
sorted_arr = optimized_bubble_sort(numbers)
print(sorted_arr)
