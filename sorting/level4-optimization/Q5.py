#Test an already sorted array and count comparisons and shifts.
[1, 2, 3, 4, 5]

def insertion_sort(arr):
    n = len(arr)
    count_of_comparisons = 0
    count_of_shifts = 0
    for i in range(1, n):
        j = i
        while(j>0):
            count_of_comparisons += 1
            if (arr[j-1]>arr[j]):
                count_of_shifts += 1
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            else:
                break
    return arr, count_of_comparisons, count_of_shifts

numbers = [1, 2, 3, 4, 5]
sorted_array, comparisons, shifts = insertion_sort(numbers)
print(sorted_array)
print(comparisons)
print(shifts)