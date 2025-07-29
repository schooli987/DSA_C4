# Function to organize t-shirt sizes on the shelf using Insertion Sort
def organize_shelf(sizes):
    for i in range(1, len(sizes)):
        key = sizes[i]
        j = i - 1
        while j >= 0 and sizes[j] > key:
            sizes[j + 1] = sizes[j]
            j -= 1
        sizes[j + 1] = key
    return sizes

# Given list of t-shirt sizes (shelf is messed up)
sizes = [40, 34, 38, 36, 42]
print("Messed up shelf:",sizes)

# Call the function and print the organized list
sorted_sizes = organize_shelf(sizes)
print("Organized display sizes:", sorted_sizes)
