#Count swaps in Selection Sort
#Count actual swaps. Avoid swapping an element with itself.
[1, 2, 3, 4, 5]

def seletion_sort(arr):
    n = len(arr)
    count_of_swaps = 0
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            count_of_swaps += 1
    return arr, count_of_swaps

numbers = [29, 10, 14, 37, 13]
sorted_arr, count_of_swaps = seletion_sort(numbers)
print(sorted_arr)
print(count_of_swaps)