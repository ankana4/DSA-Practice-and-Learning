#Optimize Bubble Sort
#Add a swapped flag. Test the array and show why the algorithm stops after the second pass.
[1, 2, 3, 5, 4]

def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        swapped=False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if swapped == False:
            break
    return arr

numbers = [1, 2, 3, 5, 4]
print(bubble_sort(numbers))        