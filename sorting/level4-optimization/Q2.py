#Remember the index of the final swap and use it as the next pass boundary.
[1, 2, 6, 3, 4, 5, 7, 8]

def bubble_sort(arr):
    n = len(arr)

    while n > 1:
        last_swap = 0

        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                last_swap = j + 1

        n = last_swap

        if last_swap == 0:
            break

    return arr


numbers = [1, 2, 6, 3, 4, 5, 7, 8]
sorted_arr = bubble_sort(numbers)

print(sorted_arr)