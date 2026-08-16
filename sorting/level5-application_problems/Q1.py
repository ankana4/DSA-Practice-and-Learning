#Sort student marks
#Use Selection Sort to sort marks in descending order.
marks = [78, 92, 65, 88, 72]
def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(marks))


#Another approach
def selection_sort_desc(arr):
    n = len(arr)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] > arr[min_index]:
                min_index=j
        if arr[min_index] != arr[i]:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

numbers = marks = [78, 92, 65, 88, 72]

print(selection_sort_desc(numbers))