#Sort by absolute value
#Sort based on abs(value), while preserving the original signs.
n = [-8, 3, -2, 7, -5]

def sort_by_abs(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j>0 and abs(arr[j-1]) > abs(arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1  
    return arr

print(sort_by_abs(n))