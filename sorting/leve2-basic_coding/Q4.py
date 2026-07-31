#Sort in descending order
#Modify all three algorithms to produce descending order.
numbers = [15, 3, 9, 1, 12]

#Selection sort code

def selection_sort_desc(arr):
    n = len(arr)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] > arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

numbers = [15, 3, 9, 1, 12]
print(selection_sort_desc(numbers))

#Bubble sort code

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [15, 3, 9, 1, 12]
print(bubble_sort_desc(numbers))  

#Insertion sort code
def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while (j>0 and arr[j-1]< arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -=1
    return arr

numbers = [15, 3, 9, 1, 12] 
print(insertion_sort_desc(numbers))                          
            