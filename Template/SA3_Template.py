# Step 1: Get sizes from user
sizes_input = input("Enter t-shirt sizes separated by spaces (e.g., S M L M S): ")

# Step 2: Convert input string to a list (no need to convert to int here)
tshirt_list = sizes_input.upper().split()  # Convert all inputs to uppercase for consistency

# Step 3: Categorize sizes into shelves
small = []
medium = []
large = []
