''' Selection Sort - Find minimum and swap '''

def selection_sort_asc(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def selection_sort_desc(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] > arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr    
numbers = [29, 10, 14, 37, 13]
sorted_arr = selection_sort_desc(numbers)
print(sorted_arr)            

