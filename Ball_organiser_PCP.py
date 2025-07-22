# Sample racks (you can later ask students to input these)
small_rack = [4, 5]              # Small-sized balls
medium_rack = [6, 7, 6]          # Medium-sized balls
large_rack = [8]                 # Large-sized balls

# Function to sort ball sizes using Insertion Sort
def sort_rack(rack):
    for i in range(1, len(rack)):
        key = rack[i]
        j = i - 1
        while j >= 0 and rack[j] > key:
            rack[j + 1] = rack[j]
            j -= 1
        rack[j + 1] = key
    return rack

# Function to check restocking need
def check_restock(rack, name):
    sorted_rack = sort_rack(rack)
    print(f"{name} Rack after sorting:", sorted_rack)
    if len(rack) < 5:
        print(f"⚠️ Restock Alert: {name} rack has only {len(rack)} ball(s).\n")

# Check each rack
check_restock(small_rack, "Small")
check_restock(medium_rack, "Medium")
check_restock(large_rack, "Large")
