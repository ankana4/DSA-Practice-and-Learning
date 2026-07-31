#Handle duplicate values
#Sort the following using all three algorithms.
[4, 2, 4, 1, 2]

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        didswapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didswapped = True
        if didswapped == False:
            break        
    return arr    


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j=i
        while(j>0 and arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr        
        
numbers = [4, 2, 4, 1, 2]
print(selection_sort(numbers.copy())) 
print(bubble_sort(numbers.copy())) 
print(insertion_sort(numbers.copy()))