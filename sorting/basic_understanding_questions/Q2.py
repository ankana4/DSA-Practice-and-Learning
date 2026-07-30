# Dry run selection sort
[29, 10, 14, 37, 13]

#Show after every pass:

#Current index i
#Minimum element found
#Swap performed
#Array after the swap

def selection_sort(arr):
    n = len(arr)
    swapped = 0
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if arr[j]< arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        swapped += 1
    return arr, swapped

numbers = [29, 10, 14, 37, 13]
sorted_arr, swapped = selection_sort(numbers)
print(sorted_arr)
print("Count of swapped is", swapped)

            