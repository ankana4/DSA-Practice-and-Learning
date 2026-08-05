#Count comparisons in Selection Sort
#Modify Selection Sort to count comparisons. For five elements, verify that the count is 4 + 3 + 2 + 1 = 10.
[29, 10, 14, 37, 13]

def selection_sort(arr):
    n = len(arr)
    count_of_comparisons = 0
    for i in range(0, n-1):
        min_index=i
        for j in range(i+1, n):
            count_of_comparisons += 1
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr, count_of_comparisons

numbers = [29, 10, 14, 37, 13]
sorted_arr, count_of_comparison = selection_sort(numbers)
print(sorted_arr)
print(count_of_comparison)             