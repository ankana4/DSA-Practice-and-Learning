#Write Bubble Sort
#Sort the following list. Do not use sort() or sorted().
numbers = [9, 7, 5, 3, 1]

def bubble_sort(arr):
    n = len(arr)
    didswapped = 0
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didswapped = 1
        if didswapped == 0:
            break        
    return arr

numbers = [9, 7, 5, 3, 1]
sorted_arr = bubble_sort(numbers)
print(sorted_arr)