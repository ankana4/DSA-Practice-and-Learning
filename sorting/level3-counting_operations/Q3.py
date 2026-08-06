#Count comparisons and swaps in Bubble Sort
#Print the total comparisons and total swaps.
[5, 4, 3, 2, 1]

def bubble_sort(arr):
    n = len(arr)
    count_of_comparisons = 0
    count_of_swaps = 0
    didswapped = False
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            count_of_comparisons += 1
            if arr[j] > arr[j+1]:
                count_of_swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didswapped = True
        if didswapped == False:
            break       
    return arr, count_of_comparisons, count_of_swaps

numbers = [5, 4, 3, 2, 1]
sorted_arr, count_of_comparisons, count_of_swaps = bubble_sort(numbers)
print(sorted_arr)
print(count_of_comparisons)
print(count_of_swaps)

