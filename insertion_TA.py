# Function to sort a list using Insertion Sort
def insertion_sort(arr):
    # Start from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]          # Current value to be inserted
        j = i - 1             # Index of previous element

        # Shift elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at its correct position
        arr[j + 1] = key
    return arr

# Example list of numbers to be sorted
sizes = [40, 34, 38, 36, 42]
print("Before sorting:", sizes)

# Call the function to sort the list
sorted_sizes = insertion_sort(sizes)
print("After sorting:", sorted_sizes)
