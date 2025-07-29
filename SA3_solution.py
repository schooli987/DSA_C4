# Function to sort t-shirt sizes using Insertion Sort in descending size order (L > M > S)
def insertion_sort(arr):
    # Define custom order
    size_order = {'L': 3, 'M': 2, 'S': 1}
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and size_order[arr[j]] < size_order[key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Step 1: Get sizes from user
sizes_input = input("Enter t-shirt sizes separated by spaces (e.g., S M L M S): ")

# Step 2: Convert input string to a list
tshirt_list = sizes_input.upper().split()

# Step 3: Sort using Insertion Sort based on size order
sorted_tshirts = insertion_sort(tshirt_list)

# Step 4: Display sorted list
print("\nSorted T-shirts for Clearance Sale:", sorted_tshirts)

# Step 5: Categorize sorted sizes into shelves
large_shelf = []
medium_shelf = []
small_shelf = []

for size in sorted_tshirts:
    if size == 'L':
        large_shelf.append(size)
    elif size == 'M':
        medium_shelf.append(size)
    elif size == 'S':
        small_shelf.append(size)

# Step 6: Display shelves
print("\n Large Shelf :", large_shelf)
print("\n Medium Shelf:", medium_shelf)
print("\n Small Shelf :", small_shelf)
