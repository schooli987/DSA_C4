# Step 1: List of t-shirts as (code, size) tuples
tshirt_list = [('T1', 40), ('T2', 34), ('T3', 38), ('T4', 36), ('T5', 42)]

# Step 2: Insertion Sort in descending order of size
for i in range(1, len(tshirt_list)):
    key_item = tshirt_list[i]
    j = i - 1
    while j >= 0 and tshirt_list[j][1] < key_item[1]:
        tshirt_list[j + 1] = tshirt_list[j]
        j -= 1
    tshirt_list[j + 1] = key_item

# Step 3: Print the sorted list
print("Clearance Sale – T-Shirts Sorted from Largest to Smallest:")
for code, size in tshirt_list:
    print(f"{code} - Size {size}")
