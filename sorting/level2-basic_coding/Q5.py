#Sort without returning
#Modify Bubble Sort so that it changes the original list directly and returns None.
numbers = [4, 2, 7, 1]
#bubble_sort(numbers)
print(numbers)

def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        didswapped = 0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didswapped = 1
        if didswapped == 0:
            break
        
numbers = [4, 2, 7, 1]
bubble_sort(numbers)
print(numbers)                