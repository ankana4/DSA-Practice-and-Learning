#Dry-run Bubble Sort for:

[5, 1, 4, 2, 8]

#Show every comparison and swap during the first two passes.

def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr            


numbers = [5,1,4,2,8]
sorted_arr = bubble_sort(numbers)
print(sorted_arr)