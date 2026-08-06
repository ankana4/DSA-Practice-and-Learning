#Write Insertion Sort
#Expected output: [5, 6, 11, 12, 13].
numbers = [12, 11, 13, 5, 6]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while(j>0 and arr[j-1] > arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

numbers = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(numbers)
print(sorted_arr)