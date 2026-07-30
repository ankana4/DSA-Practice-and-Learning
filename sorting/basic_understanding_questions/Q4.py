#Dry-run Insertion Sort for:

[7, 4, 5, 2]

#For every pass, show:

#key
#j
#elements shifted
#array after inserting the key

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while(j>0 and arr[j-1]> arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

numbers = [7,4,5,2]
sorted_arr = insertion_sort(numbers)
print(sorted_arr)        