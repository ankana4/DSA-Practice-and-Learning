#Handle one element
#Test all algorithms with [10]. What happens, and how many comparisons are made?

def selection_sort(arr):
    n = len(arr)
    count_of_comparisons = 0
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            count_of_comparisons += 1
            if arr[j] > arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr, count_of_comparisons

def bubble_sort(arr):
    n = len(arr)
    count_of_comparisons = 0
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            count_of_comparisons += 1
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, count_of_comparisons

def insertion_sort(arr):
    n = len(arr)
    count_of_comparison = 0
    for i in range(1, n):
        j = i
        while (j>0 and arr[j] < arr[j-1]):
            count_of_comparison += 1
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr, count_of_comparison


numbers = [10]
sorted_numbers, count_of_comparison = insertion_sort(numbers)
print(sorted_numbers)
print(count_of_comparison)