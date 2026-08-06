#Write Selection Sort
#Sort the list in ascending order using Selection Sort.
numbers = [64, 25, 12, 22, 11]

def selection_sort_asc(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

numbers = [64, 25, 12, 22, 11]
sorted_arr = selection_sort_asc(numbers)
print(sorted_arr)     