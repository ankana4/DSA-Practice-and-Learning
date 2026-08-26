#Make Selection Sort stable
#Instead of swapping the minimum, remove it and shift intermediate elements right. Explain the trade-off.

def stable_selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Find minimum element
        for j in range(i + 1, n):
            if arr[j][1] < arr[min_index][1]:
                min_index = j

        # Store minimum
        min_value = arr[min_index]

        # Shift elements to the right
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -= 1

        # Put minimum at its correct position
        arr[i] = min_value

    return arr


arr = [("A", 2), ("B", 2), ("C", 1)]

print(stable_selection_sort(arr))