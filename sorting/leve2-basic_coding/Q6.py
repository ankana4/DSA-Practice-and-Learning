#Handle an empty list
#Make all three functions correctly handle an empty list.

def selection_sort(arr):
    n = len(arr)
    if len(arr) == 0:
        return arr
    else:
        for i in range(0, n -1):
            min = i
            for j in range(i+1, n):
                if arr[j] < arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    if n == 0:
        return []
    else:
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    n = len(arr)
    if n == 0:
        return []
    else:
        for i in range(1, n):
            j = i
            while(j>0 and arr[j-1] > arr[j]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
    return arr


numbers = []
print(insertion_sort(numbers))        