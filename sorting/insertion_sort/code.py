''' Insertion Sort - Takes an element and place it in its correct position '''

def insertion_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        j = i
        while(j>0 and arr[j-1] > arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

numbers = [14, 9, 15, 12, 6, 8, 13]
sorted_arr = insertion_sort(numbers)
print(sorted_arr)        