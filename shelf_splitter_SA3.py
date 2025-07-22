# Function to sort a list using Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Step 1: Get sizes from user
sizes_input = input("Enter t-shirt sizes separated by spaces (e.g., S M L M S): ")

# Step 2: Convert input string to a list (no need to convert to int here)
tshirt_list = sizes_input.upper().split()  # Convert all inputs to uppercase for consistency

# Step 3: Categorize sizes into shelves
small = []
medium = []
large = []

for size in tshirt_list:
    if size == 'S':
        small.append(size)
    elif size == 'M':
        medium.append(size)
    elif size == 'L':
        large.append(size)

# Step 4: Sort each shelf using Insertion Sort
small = insertion_sort(small)
medium = insertion_sort(medium)
large = insertion_sort(large)

# Step 5: Display results
print("\n🧺 Small Shelf:", small)
print("👕 Medium Shelf:", medium)
print("🧥 Large Shelf:", large)
