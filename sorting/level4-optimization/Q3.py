#Avoid unnecessary Selection Sort swaps
#Swap only when min_index != i. Explain why this reduces writes but does not change O(n^2) time complexity.

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min=j
        if min != i:        
            arr[i], arr[min] = arr[min], arr[i]
    return arr            

numbers = [4, 2, 7, 1]
print(selection_sort(numbers))